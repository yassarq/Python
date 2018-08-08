'''Countdown - Create a function that accepts a number as an 
input.  Return a new array that counts down by one, from the 
number (as arrays 'zero'the element) down to 0 
(as the last element).  For example countDown(5) 
should return [5,4,3,2,1,0].'''
# def countDown_func(num):
#     newlist = []
#     for count in range(num,-1,-1):
#         newlist.append(count)
#     return newlist
# print(countDown_func(5))


'''Print and Return - Your function will receive an array with 
two numbers. Print the first value, and return the second.'''
# def receive_fun(list):
#     print(list[0])
#     return list[1]
# print(receive_fun([2,2]))


'''First Plus Length - Given an array, return the sum of the 
first value in the array, plus the array's length.'''
# def first_plus(list):
#     return list[0] + len(list)
# print(first_plus([1,2,3,4]))


'''Values Greater than Second - Write a function that accepts 
any array, and returns a new array with the array values that 
are greater than its 2nd value.  Print how many values this is.  
If the array is only element long, have the function return False'''

# def accepts_list(list):
#     amount = 0
#     newlist = []
#     for count in range(len(list)):
#         if list[count] > list[1]:
#             newlist.append(list[count])
#             amount+=1
#     print(amount)               
#     return newlist

# print(accepts_list([1,2,3,4]))

'''This Length, That Value - Given two numbers, return array of 
length num1 with each value num2.  Print "Jinx!" if they are same.'''

# def length_value(num1, num2):
#     newlist = []
#     if num1 == num2:
#         print("Jinx!")
#     for count in range(num1):
#         newlist.append(num2)
#         count += 1
#     return newlist
# print(length_value(6,6))