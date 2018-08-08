# Define new classes
# Add attributes that describe the state of our objects
# Add methods that describe the behavior of our objects
# Initialize our instances with the __init__() method
# Naming and passing default parameters
# Import and create new modules that we can use in our files/classes

# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.logged = True
#     def login(self):
#         self.logged = True
#         print(self.name + " is logged in.")
#         return self
#     def logout(self):
#         self.logged = False
#         print(self.name + " is not logged in")
#         return self
#     def show(self):
#         print(f"My name is {self.name}. You can email me at {self.email}.")
#         return self
# myuser = User('bob', 'emasil')


# # Self and__init__()
#     class User:
#         name="Anna"
#     anna = User()
#     print("anna's name:", anna.name)                            
#     User.name = "Bob"
#     print("anna's name after change:", anna.name)               
#     bob = User()
#     print("bob's name:", bob.name)                      

# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.logged = False
    
# user1 = User("Anna Propas", "anna@anna.com")
# print(user1.name)
# print(user1.logged)
# print(user1.email)
        

# file vehicles.py
class Vehicle:
    def __init__(self, wheels, capacity, make, model):
        self.wheels = wheels
        self.capacity = capacity
        self.make = make
        self.model = model
        self.mileage = 0
    def drive(self,miles):
        self.mileage += miles
        return self
    def reverse(self,miles):
        self.mileage -= miles
        return self

