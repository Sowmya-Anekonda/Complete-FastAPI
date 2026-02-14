from fastapi import FastAPI
from starlette.middleware.gzip import GZipMiddleware


app = FastAPI()

app.add_middleware(
    GZipMiddleware,
    minimun_size=1000 # 1000 units of memeory
)