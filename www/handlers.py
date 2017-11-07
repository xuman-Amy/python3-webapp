
# coding: utf-8

import re, time, json, logging, base64, asyncio,orm

from coroweb import get,post

from models import User,Comment,Blog, next_id

@get('/')
async def index(request):
    blogs = await Blog.findAll()
    print(blogs)
    return {
        '__template__':'blogs.html',
        'blogs' : blogs
    }

