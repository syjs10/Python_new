import os

print 'Process (%s) is start...' %os.getpid()

pid = os.fork()

if pid == 0:
	print 'I\'m child process (%s), and my father process is (%s).'%(os.getpid(), os.getppid())
else:
	print 'I (%s) just create a child process(%s).'%(os.getpid(), pid)