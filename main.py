"""
Author: Paul Owe
Date: 29 July, 2022
"""

from fastapi import FastAPI

app = FastAPI()

# The line below invokes our index method at the root
@app.get('/')
def index():

    return 'Hello AI engineering world!'
