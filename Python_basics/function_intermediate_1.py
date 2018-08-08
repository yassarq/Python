# # Create beCheerful().  Within it, print string "good morning!" 98 times.
# print("*"*80)
# def beCheerful(name='', repeat=1):
# 	print(f"good morning {name}\n"*repeat)
# beCheerful()
# beCheerful(name="john")
# beCheerful(name="michael", repeat=5)
# beCheerful(repeat=5, name="kb")
# beCheerful(name="aa")
# # helpful tips for the next assignment

# print(random.random()) # returns a random floating number between 0.000 to 1.000
# print(random.random()*50) # returns a float between 0.000 to 50.000
# int( 3.654 ) # returns 3
# round( 3.654 ) # returns 4



# from random import random 
# def randInt(min = 0, max = 100):
#      return int((random() * (max - min + 1)) + min)
# print(randInt())
# print(randInt(max = 50))
# print(randInt(min = 50))
# print(randInt(min = 50, max = 500))


# print(round(random()*50 ))


capitals = {"svk":"Bratislava","deu":"Berlin", "dnk":"Copenhagen"}
# creating a new key/value pair
capitals["abc"] = "New Country" 
# updating
capitals["abc"] = "ABC Country"
#to print all keys
for data in capitals:
     print(data)
#another way to print all keys
for key in capitals.keys():
     print(key)
#to print the values
for val in capitals.values():
     print(val)
#to print all keys and values
for key, val in capitals.items():
     print(key, " = ", val)
