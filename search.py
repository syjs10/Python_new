import os
import re
import sys

if len(sys.argv) > 1:
	for x in os.listdir('.'):
		if os.path.isfile(x):
			file = os.path.split(x)
			fileName = os.path.splitext(file[1])
			if re.match(r'.*'+sys.argv[1]+'.*', fileName[0]):
				print x
else:
	print "Please input right parameter"