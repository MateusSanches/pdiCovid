import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score
import pickle

def train_classifier(input_file, output_model):
    df = pd.read_csv(input_file)
    X = df.drop(columns=['filename', 'label'])
    y = df['label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    classifier = SVC(kernel='linear')
    classifier.fit(X_train, y_train)
    with open(output_model, 'wb') as f:
        pickle.dump(classifier, f)
        
    print("Classificador treinado e salvo com sucesso!")

if __name__ == "__main__":
    train_classifier('saida', 'modelo')