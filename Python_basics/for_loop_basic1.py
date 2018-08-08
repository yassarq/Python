'''Basic - Print all the numbers/integers from 0 to 150.'''
# for i in range(0,151):
#     print (i)

'''Multiples of Five - Print all the multiples of 5 from 5 
to 1,000,000.'''
# for i in range(5,1000000,5):
#     print (i)

'''Counting, the Dojo Way - Print integers 1 to 100.  
If divisible by 5, print "Coding" instead. 
If by 10, also print " Dojo".'''

# for i in range(1,101):
#     if i % 5 == 0:
#         print ("Coding")
#         if i % 10 == 0:
#             print ("Dojo")
#     else:
#         print (i)

'''Whoa. That Sucker's Huge - Add odd integers 
from 0 to 500,000, and print the final sum.'''

# sum = 0
# for i in range(1,500001,2):
#     sum += i
# print (sum)


'''Countdown by Fours - Print positive numbers starting 
at 2018, counting down by fours (exclude 0).'''

# for i in range(2018,1,-4 ):
#     print(i)


'''Flexible Countdown - Based on earlier "Countdown by 
Fours", given lowNum, highNum, mult, print multiples 
of mult from lowNum to highNum, using a FOR loop.  
For (2,9,3), print 3 6 9 (on successive lines)'''

# def count(low, high, mult):
#     for i in range(low, high+1):
#         if i % mult == 0:
#             print (i)
# count(2,9,3)


# list = [3,5,1,2]
# for i in list:
#     print(i)

# list = [3,5,1,2]
# for i in range(list):
#     print(i)

# list = [3,5,1,2]
# for i in range(len(list)):
#     print(i)








# def a():
#     print(5)
# x = a()
# print(x)

# def a(b,c):
#     print(b+c)
# print(a(1,2) + a(2,3))   

# def a(b,c):
#     return str(b)+str(c)
# print(a(2,5)

# def a():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(a)

# def a(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(a(2,3))
# print(a(5,3))
# print(a(2,3) + a(5,3))     

# def a(b,c):
#     return b+c
#     return 10
# print(a(3,5))     

# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
# print(b)
# a()
# print(b)  


# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# a()
# print(b)  


# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=a()
# print(b)

# def a():
#     print(1)
#     b()
#     print(2)
# def b():
#     print(3)
# a()

# def a():
#     print(1)
#     x = b()
#     print(x)
#     return 10
# def b():
#     print(3)
#     return 5
# y = a()
# print(y)