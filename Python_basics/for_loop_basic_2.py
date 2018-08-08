''' *Biggie Size* - Given an array, write a function that changes all positive numbers in the array to "big". Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5]. '''
# def positive (list):
#     for i in range (len(list)):
#         if list[i] > 0:
#             list[i] = "big"
#     return list
# print(positive ([-1, 3, 5, -5]))


'''*Count Positives* - Given an array of numbers, create a function to replace last value with number of positive values. Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.  (Note that zero is not considered to b a positive number).'''
# def replace_last (list):
#     count = 0
#     for i in range (len(list)):
#         if list[i] > 0:
#             count+=1
#     list[len(list)-1] = count
#     return list
# print(replace_last ([-1,1,1,3]))

'''*SumTotal* - Create a function that takes an array as an argument and returns the sum of all the values in the array.  For example sumTotal([1,2,3,4]) should return 10'''
# def sumTotal (list):
#     count = 0
#     for i in list:
#         count+=i
#     return count
# print(sumTotal([1,2,3]))


'''*Average* - Create a function that takes an array as an argument and returns the average of all the values in the array.  For example multiples([1,2,3,4]) should return 2.5'''
# def ave (list):
#     count = 0
#     for i in list:
#         count+=i
#     return count/len(list)
# print(ave([1,2,3,4]))

'r example length([1,2,3,4]) should return 4'''

# def length (list):
#     return len(list)
# print(length([1,2,3,4]))

'''*Minimum* - Create a function that takes an array as an argument and returns the minimum value in the array.  If the passed array is empty, have the function return false.  For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.'''
# def min (list):
#     min_value = list[0]
#     for i in range (len(list)):
#         if  list[i] < min_value:
#             min_value = list[i]
#     return min_value
# print(min([1,2,3,4]))

'''*Maximum* - Create a function that takes an array as an argument and returns the maximum value in the array.  If the passed array is empty, have the function return false.  For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -3.'''
# def max (list):
#     max_value = list[0]
#     for i in range (len(list)):
#         if  list[i] > max_value:
#             max_value = list[i]
#     return max_value
# print(max([1,2,3,4]))


'''*UltimateAnalyze* - Create a function that takes an array as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the array.'''
# def ultimate_analyze(list):
#     return{'total':sumTotal(list),'ave':ave(list),'min':min(list),'max':max(list),'length':length(list)}
# print(ultimate_analyze([9,4,2,1]))


'''*ReverseList* - Create a function that takes an array as an argument and return an array in a reversed order.  Do this without creating an empty temporary array.  For example reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.'''
# def reversed_order(list):
#     list.reverse()
#     return list
# print(reversed_order([1,2,3,4,5]))