class Dog ():
	def __init__(self,name,age):
		self.name=name
		self.age=age

	def sit (self):
		print ("Sit down", self.name)



mydog= Dog ('Dio', 33)
print mydog.name, mydog.age
mydog.sit()


class Restaurant ():
	def __init__(self, name, cuisine):
		self.name=name
		self.cuisine=cuisine
		self.number_served=0

	def describe_restaurant (self):
		print ("The name of the restaurant is " +(self.name) +" and the cuisine is " +(self.cuisine))

	def open_restaurant (self):
		print ("The restaurant is open")

	def set_number_served (self,n):
		self.number_served=n
		return self.number_served

	def increment_number_served (self,n):
		return self.number_served+n


restaurant=Restaurant ('giallorossa', 'italian')
print restaurant.name
print restaurant.cuisine
restaurant.describe_restaurant()
restaurant.open_restaurant()
print restaurant.set_number_served(10)
print restaurant.increment_number_served(5)


class User ():
	def __init__(self,firstname,lastname, *info):
		self.firstname=firstname
		self.lastname=lastname
		self.login_attempts=0
		self.info=info

	def describe_user(self):
		print (self.firstname, self.lastname, self.info)

	def greet_user(self):
		print ("Welcome "+ self.firstname +  self.lastname)

	def increment_login_attempts (self):
		self.login_attempts=self.login_attempts+1
	

	def reset_login_attempts (self):
		self.login_attempts=0

	def read_login_attempts (self):
		print ("the number of login attempts is "+ str(self.login_attempts))


user=User ('francesco', 'totti', 41, 'calciatore')
user.describe_user()
user.greet_user()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.read_login_attempts()
user.reset_login_attempts()
user.read_login_attempts()




