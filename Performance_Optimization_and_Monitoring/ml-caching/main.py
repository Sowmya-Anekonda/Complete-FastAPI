import redis
import json
import hashlib
import joblib
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
redis_client = redis.Redis(host='localhost', port=6379, db=0)

model = joblib.load('model.joblib')


class IrisFlower(BaseModel):
    sepal_length: float 
    sepal_width: float 
    petal_length: float 
    petal_width: float 

    def to_list(self):
        return [
            self.sepal_length,
            self.sepal_width,
            self.petal_length,
            self.petal_width
        ]
    
    def cache_key(self):
        raw = json.dumps(self.model_dump(), sort_keys=True)
        return f"Predict: {hashlib.sha256(raw.encode()).hexdigest()}"
    

@app.post('/predict')
async def predict(data: IrisFlower):
    key = data.cache_key()

    cached_result = redis_client.get(key)
    if cached_result:
        print('Serving prediction from Cache!')
        return json.loads(cached_result)
    
    prediction = model.predict([data.to_list()])[0]
    result = {'prediction': int(prediction)}
    redis_client.set(key, json.dumps(result), ex=3600)
    return result 