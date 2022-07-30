"""
Author: Paul Owe
Date: 29 July, 2022
"""

from fastapi import FastAPI, Response, status
from enum import Enum
from typing import Optional # In case you want to provide optional parameters for your API methods

app = FastAPI()

# The line below invokes our index method at the root path/endpoint
@app.get('/')
def index():

    return {'message': 'Hello AI engineering world!'}

# @app.get('/blog/all')
# def get_all_blogs():
#     return {'message':'All blogs fam'}

@app.get(
    '/blog/all',
    tags=['blog'],
    summary = "Gets all blogs",
    description=" Moer detailde description",
    response_description="the list of all blogs rd ")
def get_all_blogs(page_size=2, page:Optional[int] = None):
    return {'message':f'All {page_size} blogs on page {page}'}

@app.get(
    '/blog/{id}/comments/{comment_id}',
    tags=['blog', 'comment'])
def get_comment(id:int, comment_id:int, valid: bool = True, username: Optional[str]=None):
    """
     **id** - id of blog

     valid - bool

     uname - optional int 

    """
    return {'message': f'blog_id {id}, comment_id {comment_id}, valid comment? {valid}, username {username}'}

class BlogType(str, Enum):
   short='short-blog'
   story='story-blog'
   howto='howto-blog'

@app.get('/blog/type/{type}', tags=['blog'])
def get_blogs_by_type(type: BlogType):
    return {'message':f'Blogs of type {type}'} 


@app.get('/blog/{id}', status_code=status.HTTP_200_OK, tags=['blog'])
def get_blog(id:int, response: Response):
    if id> 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog id {id} not found'}
    else: 
        response.status_code = status.HTTP_200_OK 
        return {'message':f'Blog with ID {id}'}














# To run it uvicorn main:app --reload

