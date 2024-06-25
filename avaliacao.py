import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score
import pickle

def evaluate_classifier(input_model, input_file):
    df = pd.read_csv(input_file)
    X = df.drop(columns=['filename', 'label'])
    y = df['label']
    with open(input_model, 'rb') as f:
        classifier = pickle.load(f)
    y_pred = classifier.predict(X)
    print(f'Acurácia: {accuracy_score(y, y_pred)}')
    print(f'Matriz de Confusão:\n {confusion_matrix(y, y_pred)}')

if __name__ == "__main__":

    evaluate_classifier('modelo', 'saida')