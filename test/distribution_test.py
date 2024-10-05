'''
Distribution tests
Because we are assuming all variables are numerical, we only use the ks test.
'''

import pandas as pd
from scipy.stats import ks_2samp

def test_distributions():

    '''
    Function to apply the Kolmogorov-Smirnoff to the variables to check if the model needs retrain.
    '''
    new_sample: pd.DataFrame = pd.read_csv("data/stored_data.csv").iloc[-1000:, :]
    train_sample: pd.DataFrame = pd.read_csv("data/credit_train.csv")

    for column in new_sample.columns:

        test = ks_2samp(new_sample[column].values, train_sample[column].values)

        if test.pvalue < 0.5:
            print(f"Hey m8, maybe the model doesn't work. The distribution of {column} is shady")
            continue

if __name__ == "__main__":
    test_distributions()
