import os
import cv2
import numpy as np
import pandas as pd
from skimage.feature import graycomatrix, graycoprops

def extract_glcm_features(image, distances, angles):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    glcm = graycomatrix(gray_image, distances=distances, angles=angles, symmetric=True, normed=True)
    features = []
    for prop in ['contrast', 'dissimilarity', 'homogeneity', 'energy', 'correlation', 'ASM']:
        for d in range(len(distances)):
            for a in range(len(angles)):
                features.append(graycoprops(glcm, prop)[d, a])
    return features

def process_images(input_dir, output_file):
    distances = [1, 2, 3]
    angles = [0, np.pi/4, np.pi/2, 3*np.pi/4]
    data = []

    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg'):
                image_path = os.path.join(root, file)
                image = cv2.imread(image_path)
                features = extract_glcm_features(image, distances, angles)
                label = os.path.basename(root)
                data.append([file] + features + [label])
                
    columns = ['filename'] + [f'{prop}_{d}_{a}' for prop in ['contrast', 'dissimilarity', 'homogeneity', 'energy', 'correlation', 'ASM'] for d in range(len(distances)) for a in range(len(angles))] + ['label']
    df = pd.DataFrame(data, columns=columns)
    df.to_csv(output_file, index=False)

if __name__ == "__main__":

    process_images('entrada', 'saida')