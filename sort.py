#this is a inbuilt python sort method in which sort() will helps us to maintain  and sort the data in ascending or descending order which has a two parameters likely reverse - If True, the sorted list is reversed (or sorted in Descending order)

#key - function that serves as a key for the sort comparison

#The simplest difference between sort() and sorted() is: sort() changes the list directly and doesn't return any value, while sorted() doesn't change the list and returns the sorted list.

"""a=[3,1,7,2,0]
a.sort()
print("the sorted list using sort is ",a)

print("the sorted list using the sorted inbuilt function is ",sorted(a,reverse=True))"""

#similarly there are other things which has to be follwed as of above parameters


#sorting the list using key and len method

def takeSecond(random):
    return random[1]

# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
random.sort(key=takeSecond)

# print list
print('Sorted list:', random)

#now considering the dictionary to be sorted consider this following program in which
 #list of information about the employees of an office where each element is a dictionary

"this is the dictonary we are been taking "

employee=[{'Name': 'John Hopkins', 'age': 18, 'salary': 1000},{'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]

"""Here, for the first case, our custom function returns the name of each employee. Since the name is a string, Python by default sorts it using the alphabetical order.

For the second case, age (int) is returned and is sorted in ascending order.

For the third case, the function returns the salary (int), and is sorted in the descending order using reverse = True"""

def get_name(employee):
    return employee.get('Name')
       

def get_age(employee):
    return employee.get('age')

def get_salary(employee):
    return employee.get('salary')

employee.sort(key=get_salary)
print(employee)

employee.sort(key=get_name,reverse=True)
print(employee)

employee.sort(key=get_age,reverse=True)
print(employee)
