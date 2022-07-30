"""
Author: Paul Owe
Date: 29 July, 2022
"""

from fastapi import FastAPI
from enum import Enum

app = FastAPI()

# The line below invokes our index method at the root path/endpoint
@app.get('/')
def index():

    return {'message': 'Hello AI engineering world!'}

@app.get('/blog/all')
def get_all_blogs():
    return {'message':'All blogs fam'}

class BlogType(str, Enum):
   short='short-blog'
   story='story-blog'
   howto='howto-blog'

@app.get('/blog/type/{type}')
def get_blogs_by_type(type: BlogType):
    return {'message':f'Blogs of type {type}'} 


@app.get('/blog/{id}')
def get_blog(id:int):
    return {'message':f'Blog with ID {id}'}














# To run it uvicorn main:app --reload

