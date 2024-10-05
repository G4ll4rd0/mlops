'''
API Module
'''
import pickle

import pandas as pd
import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from utils import init_db
from utils.init_db import SessionLocal, engine

app = FastAPI()

init_db.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

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
def predict(data: list[float], db: Session = Depends(get_db)):
    '''Prediction Endpoint'''
    x = [{f'X{i+1}': x for i, x in enumerate(data)}]
    df = pd.DataFrame.from_records(x)
    prediction = model.predict(df)
    y = int(prediction[0])

    # Save DataPoints for future examination
    credit_model        = init_db.Credit()
    credit_model.Y      = y # type: ignore
    credit_model.X1     = data[0] # type: ignore
    credit_model.X2     = data[1] # type: ignore
    credit_model.X3     = data[2] # type: ignore
    credit_model.X4     = data[3] # type: ignore
    credit_model.X5     = data[4] # type: ignore
    credit_model.X6     = data[5] # type: ignore
    credit_model.X7     = data[6] # type: ignore
    credit_model.X8     = data[7] # type: ignore
    credit_model.X9     = data[8] # type: ignore
    credit_model.X10    = data[9] # type: ignore
    credit_model.X11    = data[10] # type: ignore
    credit_model.X12    = data[11] # type: ignore
    credit_model.X13    = data[12] # type: ignore
    credit_model.X14    = data[13] # type: ignore
    credit_model.X15    = data[14] # type: ignore
    credit_model.X16    = data[15] # type: ignore
    credit_model.X17    = data[16] # type: ignore
    credit_model.X18    = data[17] # type: ignore
    credit_model.X19    = data[18] # type: ignore
    credit_model.X20    = data[19] # type: ignore
    credit_model.X21    = data[20] # type: ignore
    credit_model.X22    = data[21] # type: ignore
    credit_model.X23    = data[22] # type: ignore

    db.add(credit_model)
    db.commit()

    return {'prediction': y}

if __name__ == '__main__':
    uvicorn.run('app:app', port = 1234, reload = True)
