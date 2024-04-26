from fastapi import FastAPI
from routes.connect import *

app = FastAPI(title="Connect")
app.include_router(connect)