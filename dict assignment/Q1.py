# ***************Question 1 ************
# Write a Python script to sort (ascending and descending) a dictionary by value.
# k= {"Rahul": 75, "Anshul": 92, "Aman": 68, "Priya": 85, "Riya": 55}
# a = dict(sorted(k.items(), key=lambda x: x[1]))
# d = dict(sorted(k.items(), key=lambda x: x[1], reverse=True))
# print(a)
# print(d)

# ************Question 2*****************
# Write a Python script to add a key to a dictionary.   
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
# k={0:10,1:20}
# n=int(input("Enter Key u want to add:"))
# n2=int(input("Enter Value u want to add:"))
# k.setdefault(n,n2)
# print(k)

# *************Question 3 *****************
# Write a Python script to concatenate following dictionaries to create a new one.   
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# d1={1:10,2:20}
# d2={3:30,4:40}
# d3={5:50,6:60}
# d1.update(d2)
# d1.update(d3)
# print(d1)

# **************Question 4 ***************
# Write a Python script to check if a given key already exists in a dictionary.
# k= {"Rahul": 75, "Anshul": 92, "Aman": 68, "Priya": 85, "Riya": 55}
# n=input("Enter key u want to search:")
# if(n in k.keys()):
#     print("Yes it is there..")
# else:
#     print("not found...")

# ***********Question 5 ************
# Write a Python program to iterate over dictionaries using for loops.
# k= {"Rahul": 75, "Anshul": 92, "Aman": 68, "Priya": 85, "Riya": 55}
# for i in k:
#     print(i,k[i])

# **************Question 6 **************
# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).   
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# d={}
# n=int(input("Enter number:"))
# for i in range(1,n+1):
#     d.setdefault(i,i*i)
# print(d)

# ****************Question 7 ******************
# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.   
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
# d={}
# for i in range(1,16):
#     d.setdefault(i,i*i)
# print(d)

# **************Question 8 *****************
# Write a Python script to merge two Python dictionaries.
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic1.update(dic2)
# print(dic1)

# **************Question 9 ***************
# Write a Python program to iterate over dictionaries using for loops.
# k= {"Rahul": 75, "Anshul": 92, "Aman": 68, "Priya": 85, "Riya": 55}
# for i in k:
#     print(i,k[i])

# ***************Question 10 *************
# Write a Python program to sum all the items in a dictionary.  
# k= {"Rahul": 75, "Anshul": 92, "Aman": 68, "Priya": 85, "Riya": 55}
# t=sum(k.values())
# print(t) 

# ***************Question 11 *************
# Write a Python program to multiply all the items in a dictionary.   
# k= {"Rahul": 75, "Anshul": 92, "Aman": 68, "Priya": 85, "Riya": 55}
# m=1
# for i in k:
#     m=m*k[i]
# print(m)

# ***************Question 12 *************
# Write a Python program to remove a key from a dictionary.   
# k= {"Rahul": 75, "Anshul": 92, "Aman": 68, "Priya": 85, "Riya": 55}
# k.pop("Aman")
# print(k)

# ****************Question 13 ***********
# Write a Python program to map two lists into a dictionary.
# keys   = ["Name", "Age", "City"]
# values = ["Anshul", 19, "Gwalior"]
# d={}
# for i in range(len(keys)):
#     d.setdefault(keys[i],values[i])
# print(d)

# ***************Question 14 **************
# Write a Python program to sort a dictionary by key.   
# k= {"Rahul": 75, "Anshul": 92, "Aman": 68, "Priya": 85, "Riya": 55}
# t=dict(sorted(k.items(),key=lambda a: a[0]))
# print(t)

# ***************Question 15 **************
# Write a Python program to get the maximum and minimum value in a dictionary.
# d= {"Rahul": 75, "Anshul": 92, "Aman": 68, "Priya": 85, "Riya": 55}
# k=d.values()
# print(max(k))
# print(min(k))

# ****************Question 16 ************incomplete...
# Write a Python program to get a dictionary from an object's fields.

# ***************Question 17 **********
# Write a Python program to remove duplicates from Dictionary.
# d= {"Rahul": 75, "Anshul": 92, "Aman": 92, "Priya": 85, "Riya": 55}
# d2=d.copy()
# t=[]
# for i in d:
#     if(d[i] in t):
#         d2.pop(i)
#     else:
#         t.append(d[i])
# print(d2)

# **************Question 18 ************
# Write a Python program to check a dictionary is empty or not.
# d= {"Rahul": 75, "Anshul": 92, "Aman": 92, "Priya": 85, "Riya": 55}
# if(any(d)):
#     print("not empty...")
# else:
#     print("Empty...")

# ***************Question 19 *************
# Write a Python program to combine two dictionary adding values for common keys.   
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d={}
# for i in d1:
#     if(i in d2):
#         d.setdefault(i,d1[i]+d2[i])
#     else:
#         d.setdefault(i,d1[i])
# d2.update(d)
# print(d2)

# ****************Question 20 *************
# Write a Python program to print all unique values in a dictionary.   
# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

d=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
t=[]
for i in d:
    for j in i:
        if(i[j] not in t):
            t.append(i[j])
print(t)