# *****************Question 21 **************
# Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.   
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd
# d={'1':['a','b'],'2':['c','d']}
# l1=d['1']
# l2=d['2']
# # print()
# for i in l1:
#     for j in l2:
#         print(i,j,sep='')

# ****************Question 22 ***************
# Write a Python program to find the highest 3 values in a dictionary
# d={"A": 50, "B": 90, "C": 30, "D": 80, "E": 100}
# l=list(d.values())
# l.sort(reverse=True)
# print(l[:3])

# ***************Question 23 **************
# Write a Python program to combine values in python list of dictionaries.   
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})

# l=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# d={}
# for i in l:
#     item = i['item']
#     amount = i['amount']
#     if(i['item'] in d):
#         d[item]+=amount
#     else:
#         d[item]=amount
# print(d)

# ***************Question 24 ****************
# Write a Python program to create a dictionary from a string.   
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
# d={}
# n=input("Enter string:")
# for i in n:
#     d.setdefault(i,n.count(i))
# print(d)

# ***************Question 25 ***************
# Write a Python program to print a dictionary in table format.
# d={"Rahul": 75, "Anshul": 92, "Aman": 68}
# print(f"Name\t\tMarks")
# for i in d:
#     print(f"{i}\t\t{d[i]}")

# ***************Question 26 ***************
# Write a Python program to count the values associated with key in a dictionary.   
# Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
# Expected result: Count of how many dictionaries have success as True
# d=[{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
# c=0
# for i in d:
#     if(i['success']==True):
#         c+=1
# print(c)

# ***************Question 27 *************incomplete....
# Write a Python program to convert a list into a nested dictionary of keys.

# **************Question 28 *************
# . Write a Python program to sort a list alphabetically in a dictionary.
# d = {"fruits": ["mango", "apple", "banana"],"colors": ["red", "blue", "green"]}
# d1={}
# for i in d:
#     s=sorted(d[i])
#     d1.setdefault(i,s)
# print(d1)

# **************Question 29 **************
# Write a Python program to remove spaces from dictionary keys.
# d={"first name": "Anshul", "phone number": "123"}
# d1={}
# for i in d:
#     if(' ' in i):
#         s=i.replace(' ',"")
#         d1.setdefault(s,d[i])
# print(d1)

# ****************Question 30 *****************
# Write a Python program to get the top three items in a shop.   
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3

# data={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# t=data.values()
# t=sorted(t,reverse=True)
# t=t[:3]
# for i in data:
#     if(data[i] in t):
#         print(i,data[i])

# ************Question 31 *******************
# Write a Python program to get the key, value and item in a dictionary.
# d = {"Rahul": 75, "Anshul": 92}
# print(list(d.values()))
# print(list(d.keys()))
# print(list(d.items()))

# ***********Question 32 *****************
# Write a Python program to print a dictionary line by line.
# d = {"Rahul": 75, "Anshul": 92, "Aman": 68}
# for i in d:
#     print(i,d[i])

# ***********Question 33 ****************
# Write a Python program to check multiple keys exists in a dictionary.   
# d = {"Rahul": 75, "Anshul": 92, "Aman": 68}
# l=["Rahul", "Anshul"]
# c=0
# for i in l:
#     if (i in d):
#         c+=1
# if(c==len(l)):
#     print("All exist..")

# *************Question 34 *************
# Write a Python program to count number of items in a dictionary value that is a list. 
# d = {"A": [10, 20, 30],"B": [40, 50],"C": [60, 70, 80, 90]}
# c=0
# for i in d:
#     c=c+len(d[i])
# print(c)

# *************Question 35 **************
# Write a Python program to sort Counter by value.   
# Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
# Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]
# d={'Math':81, 'Physics':83, 'Chemistry':87}
# t=d.values()
# t=sorted(t,reverse=True)
# l=[]
# for i in t:
#     for j in d:
#         if(i==d[j]):
#             u=(j,d[j])
#             l.append(u)
# print(l)

# **************Question 36 **************
# Write a Python program to create a dictionary from two lists without losing duplicate values.   
# Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
# Expected Output: defaultdict(<class 'set'>, {'Class-VII': {2}, 'Class-VI': {2}, 'Class-VIII': {3}, 'Class-V': {1}})

# Classes = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
# Values  = [1, 2, 2, 3]
# d={}
# for i in range(len(Classes)):
#     d.setdefault(Classes[i],Values[i])
# print(d)

# **************Question 37 *************
# Write a Python program to replace dictionary values with their sum.
# d = {"a": 10, "b": 20, "c": 30}
# t=sum(d.values())
# d1={}
# for i in d:
#     d1.setdefault(i,t)
# print(d1)

# *************Question 38 ************
# Write a Python program to match key values in two dictionaries.   
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y

# x = {'key1': 1, 'key2': 3, 'key3': 2}
# y = {'key1': 1, 'key2': 2}
# for i in x:
#     if i in y and x[i] == y[i]:
#         print(f"{i}:{x[i]} is present in both x and y..")

# *************Question 39 ****************incomplete...
# Write a Python program to store a given dictionary in a json file.   
# Original dictionary:
# {'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'}, {'firstName': 'Mervin', 'lastName': 'Friedland'}, {'firstName': 'Aron ', 'lastName': 'Wilkins'}], 'teachers': [{'firstName': 'Amberly', 'lastName': 'Calico'}, {'firstName': 'Regine', 'lastName': 'Agtarap'}]}
# <class 'dict'>
# Json file to dictionary:
# {'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'}, {'firstName': 'Mervin', 'lastName': 'Friedland'}, {'firstName': 'Aron ', 'lastName': 'Wilkins'}], 'teachers': [{'firstName': 'Amberly', 'lastName': 'Calico'}, {'firstName': 'Regine', 'lastName': 'Agtarap'}]}

# *************Question 40 **************
# Write a Python program to create a dictionary of keys x, y, and z where each key has as value a list from 11-20, 21-30, and 31-40 respectively. Access the fifth value of each key from the dictionary.   
# {'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
# 'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
# 'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
# 15
# 25
# 35
# x has value [11, 12, 13, 14, 15, 16, 17, 18, 19]
# y has value [21, 22, 23, 24, 25, 26, 27, 28, 29]
# z has value [31, 32, 33, 34, 35, 36, 37, 38, 39]

d = {'x': [11,12,13,14,15,16,17,18,19,20],'y': [21,22,23,24,25,26,27,28,29,30],'z': [31,32,33,34,35,36,37,38,39,40]}
print(d['x'][4])
print(d['y'][4])
print(d['z'][4])