'''
API Module
'''
import pickle

import pandas as pd
import uvicorn
from fastapi import FastAPI

app = FastAPI()

with open('./models/logistic.pkl', 'rb') as file:
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
    return {'prediction': int(prediction[0])}

if __name__ == '__main__':
    uvicorn.run('app:app', port = 1234, reload = True)
