import orm , asyncio,sys,time,json

from models import User, Blog, Comment

async def test(loop):
    summary = 'I love python'
    await orm.create_pool(loop=loop,user='root', password='123456', db='awesome')
    blogs = [
	    Blog(user_id = '11',user_name = '11', user_image = 'about:blank',name='Test Blog', summary=summary, content = summary,created_at=time.time()-120),
        Blog(user_id = '22',user_name = '22', user_image = 'about:blank',name='Something New', summary=summary, content = summary,created_at=time.time()-360),
        Blog(user_id = '33',user_name = '33', user_image = 'about:blank',name='Learn Swift', summary=summary, content = summary,created_at=time.time()-1200)
        ]
    for blog in blogs:
        await blog.save()
    
loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
if loop.is_closed():
    sys.exit(0)