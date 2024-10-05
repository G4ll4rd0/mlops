'''
Training module
'''
import os
import pickle

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Normalizer

SEED = 20020906

# TODO: Create better model
def main():
    '''Main training
    '''
    data = pd.read_csv('./data/credit_train.csv')
    x = data.drop('Y', axis = 1)
    y = data.Y

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = SEED)

    pipe = make_pipeline(Normalizer(), LogisticRegression(random_state=SEED))
    pipe.fit(x_train, y_train)

    y_hat_train = pipe.predict(x_train)
    y_hat_test = pipe.predict(x_test)

    f1_train = f1_score(y_train, y_hat_train)
    f1_test = f1_score(y_test, y_hat_test)

    accuracy_train = accuracy_score(y_train, y_hat_train)
    accuracy_test = accuracy_score(y_test, y_hat_test)

    print('F1 score train: ', f1_train)
    print('F1 score test: ', f1_test)
    print('Accuracy score train: ', accuracy_train)
    print('Accuracy score test: ', accuracy_test)

    #Saving model
    os.makedirs('./models', exist_ok=True)
    with open('./models/logistic.pkl', 'wb') as file:
        pickle.dump(pipe, file)

if __name__ == '__main__':
    main()
