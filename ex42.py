## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## Dog is an Animal
class Dog(Animal):

	def __init__(self, name):
		## Dog has an name
		self.name = name

## Cat is an Animal
class Cat(Animal):

	def __init__(self, name):
		## Cat has a name
		self.name = name

## Person is-a object
class Person(object):
	def __init__(self, name):
		self.name = name

		self.pet = None

class Employee(Person):

	def __init__(self, name, salary):
		super(Employee, self).__init__(name)
		self.salary = salary

class Fish(object):
	pass

class Salmon(Fish):
	pass

class Halibut(Fish):
	pass

rover = Dog("Rover")

satan = Cat("Satan")

flipper = Fish()

crouse = Salmon()

harry = Halibut()