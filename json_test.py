import json

class Student(object):
	"""docstring for Student"""
	def __init__(self, name, age, score):
		self.name  = name
		self.age   = age
		self.score = score
# stu = Student('Bob', 22, 99)
# # def student2dict(stu):
# # 	return {
# # 		'name' : stu.name,
# # 		'age'  : stu.age,
# # 		'score': stu.score
# # 	}


# # print (json.dumps(stu, default=student2dict))
# # 
# # ##########
# print(json.dumps(stu, default=lambda obj: obj.__dict__))


#def dict2student(d):
#	return Student(d['name'], d['age'], d['score'])
#json_str = '{"age": 20, "score": 88, "name": "Bob"}'
#print(json.loads(json_str, object_hook=dict2student))
