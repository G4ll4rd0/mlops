'''
Training module
'''
import os
import pickle

import pandas as pd
from hyperopt import STATUS_OK, Trials, fmin, hp, tpe
from hyperopt.pyll import scope
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score
from sklearn.model_selection import train_test_split

SEED = 20020906

def main():
    '''
    Main training
    '''
    data = pd.read_csv('./data/credit_train.csv')
    data.drop_duplicates(inplace = True)

    x = data.drop('Y', axis = 1)
    y = data.Y

    drop_cols = []
    for col in x.columns:
        tmpS = data[col]
        az = len(tmpS.loc[tmpS.values == 0])
        crit = az/len(data)*100
        if crit > 45:
            drop_cols.append(col)
    x = x.drop(drop_cols, axis = 1)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = SEED)

    def objective(params):
        # Train model
        booster = HistGradientBoostingClassifier(**params).fit(x_train, y_train)

        # Predict in the val dataset
        y_pred = booster.predict(x_test)

        # Calculate metric
        ps = precision_score(y_test, y_pred)
        rmse = 1 - ps

        return {'loss': rmse, 'status': STATUS_OK}

    search_space = {
        'max_depth': scope.int(hp.quniform('max_depth', 4, 100, 1)),
        'max_leaf_nodes': scope.int(hp.quniform('max_leaf_nodes', 4, 100, 1)),
        'min_samples_leaf': scope.int(hp.quniform('min_samples_leaf', 4, 100, 1)),
        'max_bins': scope.int(hp.quniform('max_bins', 2, 255, 1)),
        'learning_rate': hp.loguniform('learning_rate', -3, 0),
        'l2_regularization': hp.loguniform('l2_regularization', -6, -1),
        'random_state': SEED
    }

    best_params = fmin(
        fn=objective,
        space=search_space,
        algo=tpe.suggest,
        max_evals=1000,
        trials=Trials()
    )

    best_params["max_depth"] = int(best_params["max_depth"]) # type: ignore
    best_params["max_leaf_nodes"] = int(best_params["max_leaf_nodes"]) # type: ignore
    best_params["max_bins"] = int(best_params["max_bins"]) # type: ignore
    best_params["min_samples_leaf"] = int(best_params["min_samples_leaf"]) # type: ignore
    best_params["random_state"] = SEED # type: ignore

    best_booster = HistGradientBoostingClassifier(**best_params).fit(x_train, y_train) # type: ignore

    y_hat_train = best_booster.predict(x_train)
    y_hat_test = best_booster.predict(x_test)


    f1_train = f1_score(y_train, y_hat_train)
    f1_test = f1_score(y_test, y_hat_test)

    accuracy_train = accuracy_score(y_train, y_hat_train)
    accuracy_test = accuracy_score(y_test, y_hat_test)

    precision_train = precision_score(y_train, y_hat_train)
    precision_test = precision_score(y_test, y_hat_test)

    print('F1 score train: ', f1_train)
    print('F1 score test: ', f1_test)
    print('Accuracy score train: ', accuracy_train)
    print('Accuracy score test: ', accuracy_test)
    print('Precision score train: ', precision_train)
    print('Precision score test: ', precision_test)

    #Saving model
    os.makedirs('./.artifacts', exist_ok=True)
    with open('./.artifacts/HistGradBoost.pkl', 'wb') as file:
        pickle.dump(best_booster, file)

if __name__ == '__main__':
    main()
