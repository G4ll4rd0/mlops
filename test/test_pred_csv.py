from demo import test_api_request
import pandas as pd

dataToPredict = pd.read_csv("./data/credit_pred.csv")
dataToPredict["Y"] = dataToPredict.apply(lambda row: test_api_request(row.tolist())["prediction"], axis = 1)
dataToPredict.to_csv("./data/credit_pred.csv")
