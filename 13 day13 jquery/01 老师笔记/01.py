



class Animal(object):
	def __init__(self,name,age):
		self.name=name
		self.age=age

alex=Animal("alex",123)

attr="name"

# print(alex.attr)
print(getattr(alex,attr))


class MyList(list):
	def foo(self):
		print("foo")

ml=MyList([1,2,333])
ml.append(123)
print(ml) # [1, 2, 333, 123]
print(ml.foo())
