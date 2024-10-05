from .demo import test_api_request
import pandas as pd

dataToPredict = pd.read_csv("../data/credit_pred.csv")
dataToPredict["Y"] = dataToPredict.apply(lambda row: test_api_request(row)["predict"], axis = 1)
dataToPredict.to_csv("../data/credict_pred.csv")
