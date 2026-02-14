from fastapi import FastAPI, HTTPException
from schemas import InputSchema, OutputSchema
from predict import make_prediction, make_batch_prediction
from typing import List


app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Welcome to the ML Model prediction'}

@app.post('/prediction', response_model=OutputSchema)
def predict(user_input: InputSchema):
    # model_dump() will implicitly convert the json object to a python dictionary.
    # API expects input data in the json format. after that with the help of model_dump() converts to dict

    prediction = make_prediction(user_input.model_dump())
    return OutputSchema(pridicted_price=round(prediction, 2))

@app.post('/batch_prediction', response_model=List[OutputSchema])
def batch_predict(user_inputs: List[InputSchema]):
    predictions = make_batch_prediction([x.model_dump() for x in user_inputs])
    return [OutputSchema(pridicted_price=round(prediction, 2)) for prediction in predictions]