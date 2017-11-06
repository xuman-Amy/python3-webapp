
# coding: utf-8

# In[ ]:


import re, time, json, logging, base64, asycnio

from coroweb import get,post

from models import User,Comment,Blog, next_id

@get('/')
async def index(request):
    users = await User.findAll()
    return {
        '__template__':'test.html'
        'users':'users'
    }

