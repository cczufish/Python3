class Student(object):
	def __init__(self,name,score):
		self.__name = name
		self.__score = score

	def print_score(self):
		print('%s: %s' % (self.name,self.score))

	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'
	def get_name(self):
		return self.__name
	def get_score(self):
		return self.__score

	def set_score(self,score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('bad score')

	def set_name(self.name):
		self.__name = name



bart = Student('bart simpson',59)
lisa = Student('lisa simpon',87)
bart.print_score()
lisa.print_score()

bart.get_grade()


class Animal(object):
	def run(self):
		print('Animal is running....')


class Dog(Animal):
	def run(self):
		print('Dog is running,,.,,,')

	def eat(self):
		print('Eating meat....')

		

class Cat(Animal):
	pass


dog = Dog()
dog.run()

cat = Cat()
cat.run()



