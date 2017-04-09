# try:
# 	print 'try...'
# 	r = 10 / 'a'
# 	print 'result:', r
# except StandardError, e:
# 	print 'except:', e
import logging
def foo(s):
	return 10 / int(s)
def bar(s):
	return foo(s) * 2
def main():
	try:
		bar('a')
	except StandardError, e:
		
		logging.exception(e)
	
main();
print "hello"