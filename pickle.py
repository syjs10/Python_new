#cPickel faster than pickle 
#If cPickle can't be imported ,we import pickle
try:
	import cPickle as pickle
except ImprotError:
	import pickle
d = dict(name = 'Bob', age = 22, score = 88)
p = pickle.dumps(d)
f = open('dump.txt', 'wb')
f.write(p)
f.close()
f = open('dump.txt', 'rb')
print pickle.load(f)
f.close()