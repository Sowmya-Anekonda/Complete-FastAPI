import time 

from fastapi import FastAPI 

app = FastAPI()


def compute(n: int):
    res = 0
    for i in range(n):
        res += i 

    time.sleep(1)
    return res 


@profile 
def process_data(x: int):
    return compute(x)

@app.get('/profiling')
def profiling(a: int):
    return {'result': process_data(a)}