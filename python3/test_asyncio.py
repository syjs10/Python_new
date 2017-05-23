import threading
import asyncio

@asyncio.coroutine
def hello():
	print("Hello world! %s" % threading.currentThread())
	#异步调用 asyncio.sleep(1)
	r = yield from asyncio.sleep(1)
	print ("Hello again! %s" % threading.currentThread())

#获取EventLoop
loop = asyncio.get_event_loop()
#执行 coroutine
task = [hello(), hello()]
loop.run_until_complete(asyncio.wait(task))

loop.close()