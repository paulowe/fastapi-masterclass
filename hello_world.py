"""
Author: Paul Owe
Date: 29 July, 2022
"""

from fastapi import FastAPI

app = FastAPI()

# The line below invokes our index method at the root path/endpoint
@app.get('/')
def index():

    return {'message': 'Hello AI engineering world!'}

# To run it uvicorn hello_world:app --reload