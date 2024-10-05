'''
API Module
'''
import pickle

import pandas as pd
import uvicorn
from fastapi import FastAPI

app = FastAPI()

with open('./.artifacts/logistic.pkl', 'rb') as file:
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
    x = [{f'X{i+1}': x for i, x in enumerate(data)}]
    df = pd.DataFrame.from_records(x)
    prediction = model.predict(df)
    y = int(prediction[0])

    # Store Data
    df['Y'] = y
    path_stored = './.artifacts/stored_data.csv'
    try:
        stored_df = pd.read_csv(path_stored)
        pd.concat([stored_df, df], ignore_index=True).to_csv(path_stored, index = False)
    except:
        df.to_csv(path_stored, index=False)

    return {'prediction': y}

@app.get('/datapoints')
def datapoints():
    '''Retrieve all stored data'''
    data = pd.read_csv('./.artifacts/stored_data.csv')
    return data.to_json(orient='records', lines=True).splitlines()

if __name__ == '__main__':
    uvicorn.run('app:app', port = 1234, reload = True)
