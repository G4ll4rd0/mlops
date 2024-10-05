'''
API Module
'''
import pickle

import pandas as pd
from test.distribution_test import test_distributions
import uvicorn
from fastapi import FastAPI

app = FastAPI()

with open('./.artifacts/HistGradBoost.pkl', 'rb') as file:
    model = pickle.load(file)

@app.get('/')
def greet(name: str):
    '''Greets user'''
    return {'message': f'Hello {name}'}

@app.get('/health')
def health_check():
    '''Health Check'''
    return {'status': 'OK'}

@app.post('/predict')
def predict(data: list[float]):
    '''Prediction Endpoint'''

    z = {f'X{i+1}': x for i, x in enumerate(data)}
    x = [z]
    df = pd.DataFrame.from_records(x).drop(['X10', 'X11', 'X6', 'X7', 'X8', 'X9'], axis = 1)
    prediction = model.predict(df)
    y = int(prediction[0])

    # Store Data
    df['Y'] = y
    path_stored = './data/stored_data.csv'
    try:
        stored_df = pd.read_csv(path_stored)
        pd.concat([stored_df, df], ignore_index=True).to_csv(path_stored, index = False)
    except:
        df.to_csv(path_stored, index=False)
    
    with open("data/stored_data.csv") as stored_data:
        pito = len(stored_data.readlines())

        if pito % 1_000 == 0:
            test_distributions()

    return {'prediction': y}

@app.get('/datapoints')
def datapoints():
    '''Retrieve all stored data'''
    data = pd.read_csv('./.artifacts/stored_data.csv')
    return data.to_json(orient='records', lines=True).splitlines()

if __name__ == '__main__':
    uvicorn.run('app:app', port = 1234, reload = True)
