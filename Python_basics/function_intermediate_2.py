    given
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

    solutions
x[1][0] = 15
print(x)

students[0]['last_name']= 'Bryant'
print(students)

sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

z[0]['y'] = 30
print(z)

#     problem
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]



#     # solution
# for stu in students:
#     print('first_name','-', stu['first_name'],',','last_name','-', stu['last_name'])


    # problem
# students = [
#      {'first_name':  'Michael'},
#      {'first_name' : 'John'},
#      {'first_name' : 'Mark'},
# ]
#     # solution
# for stu in students:
#     print(stu['first_name'])



# dojo = {
#    'location': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }

# for key, val in dojo.items():
#     print(len(val), 'LOCATIONS')
#     for i in val:
#         print(i)