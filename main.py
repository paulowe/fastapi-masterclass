"""
Author: Paul Owe
Date: 29 July, 2022
"""

from fastapi import FastAPI
from router import blog_get
from router import blog_post


app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
# The line below invokes our index method at the root path/endpoint
@app.get('/')
def index():

    return {'message': 'Hello AI engineering world!'}




# To run it uvicorn main:app --reload

