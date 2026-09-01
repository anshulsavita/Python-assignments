# *******************Question 1 *****************
# A block of publicly traded stock has a variety of attributes, we'll look at a few of them. A stock has a ticker symbol and a company name. Create a simple dict with ticker symbols and company names.
# For example:
# stockDict = { 'GM': 'General Motors', 
#  'CAT':'Caterpillar', 'EK':"Eastman Kodak" }
# Create a simple list of blocks of stock. These could be tuples with ticker symbols, prices, dates and number of shares. For example:
# purchases = [ ( 'GE', 100, '10-sep-2001', 48 ), 
#  ( 'CAT', 100, '1-apr-1999', 24 ), 
#  ( 'GE', 200, '1-jul-1998', 56 ) ]
# Create a purchase history report that computes the full purchase price (shares times dollars) for each block of stock and uses the stockDict to look up the full company name. This is the basic relational database join algorithm between two tables.
# Create a second purchase summary that which accumulates total investment by ticker symbol. In the above sample data, there are two blocks of GE. These can easily be combined by creating a dict where the key is the ticker and the value is the list of blocks purchased. The program makes one pass through the data to create the dict. A pass through the dict can then create a report showing each ticker symbol and all blocks of stock.

# stockDict={
#     'GM':'General Motors',
#     'CAT':'Caterpillar',
#     'EK':'Eastman Kodak',
#     'GE':'General Electric'
# }
# purchases = [
#     ('GE', 100, '10-sep-2001', 48),
#     ('CAT', 100, '1-apr-1999', 24),
#     ('GE', 200, '1-jul-1998', 56)
# ]
# print(f"Ticker\tCompany\t\t\tPrice\tDate\t\tShares\ttotal")
# print("-------------------------------------------------------------------------------------------")
# for i in range(len(purchases)):
#     t=purchases[i][1]*purchases[i][3]
#     company=stockDict[purchases[i][0]]
#     print(f"{purchases[i][0]}\t{company.ljust(16)}\t${purchases[i][1]}\t{purchases[i][2]}\t{purchases[i][3]}\t${t}")
# print("-------------------------------------------------------------------------------------------")
# print()

# summary = {'GE': [
#         ('GE', 100, '10-sep-2001', 48),
#         ('GE', 200, '1-jul-1998', 56)],
#     'CAT': [('CAT', 100, '1-apr-1999', 24)]
# }

# print("-----------------------------------------------------")
# print("Ticker\tPrice\tDAte\t\tShares\tInvestment")
# print("-----------------------------------------------------")
# for i in summary:
#     t1=0
#     print(i)
#     for j in summary[i]:
#         t=j[1]*j[3]
#         t1=t1+t
#         print(f"\t{j[1]}\t{j[2]}\t{j[3]}\t{t}")
#     print("\t--------------------------------------")
#     print(f"\tTotal Investment\t\t{t1}")
# print("------------------------------------------------------")

# *************Question 2 ***********************
# Write a function called accept login(users, username, password) with three parameters: users a dictionary of username keys and password values, username a string for a login name and password a string for a password. The function should return True if the user exists and the password is correct and False otherwise. Here is the calling code, test your code with both good and bad passwords as well as non-existent login names: 
# users = { "user1" : "password1", "user2" : "password2", "user3" : "password3" }
#  if accept_login(users, "wronguser", "wrongpassword") :
#  print("login successful!") 
# else : 
# print("login failed...")

# def accept_login(users,username,password):
#     if(username in users.keys() and password ==users[username]):
#         return True
#     else:
#         return False
# d={ "Anshul" : "password1", "Rohit" : "password2", "Ashwini" : "password3" }
# k1=accept_login(d,"Anshul","password1")
# print(k1)

# *************Question 3 ************************
# Write a function to invert a dictionary. It should accept a dictionary as a parameter and return a dictionary where the keys are values from the input dictionary and the values are lists of keys from the input dictionary. 
# For example, this input: { "key1" : "value1", "key2" : "value2", "key3" : "value1" }
#  Should return this
#  Dictionary: { "value1" : ["key1", "key3"], "value2" : ["key2"] }

# def invert(dic):
#     keys=list(dic.keys())
#     value=list(dic.values())
#     v=[]
#     d={}
#     for i in dic:
#         l=[]
#         if(dic[i] not in v):
#             for j in range(len(value)):
#                 if(value[j]==dic[i]):
#                     l.append(keys[j])
#                     v.append(dic[i])
#             d.setdefault(dic[i],l)
#     return d
# u={ "key1" : "value1", "key2" : "value2", "key3" : "value1" }
# k=invert(u)
# print(k)

# ******************Question 4 **********************
# Write a function called word frequencies(mylist) that accepts a list of strings called mylist and returns a dictionary where the keys are the words from mylist and the values are the number of times that word appears in mylist: 
# word_list = list("aaaaabbbbcccdde") 
# word_freq = { 'a' : 5, 'b' : 4, 'c' : 3, 'd' : 2, 'e' : 1 }
# if word_frequencies(word_list) == word_freq :
#     print("correct") 
# else :
#     print("wrong")

# def word_frenquencies(mylist):
#     l=[]
#     d={}
#     for i in mylist:
#         if(i not in l):
#             d.setdefault(i,mylist.count(i))
#             l.append(i)
#     return d
# ml=list("aaaaabbbbcccdde")
# k=word_frenquencies(ml)
# print(k)


# *****************Question 5 ********************
# Given the following dictionary:
# inventory = {
#     'gold' : 500,
#     'pouch' : ['flint', 'twine', 'gemstone'],
#     'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
# }
# Try to do the followings:
# •	Add a key to inventory called 'pocket'.
# •	Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'.
# •	.sort()the items in the list stored under the 'backpack' key.
# •	Then .remove('dagger') from the list of items stored under the 'backpack' key.
# •	Add 50 to the number stored under the 'gold' key.

# inventory = {
#     'gold' : 500,
#     'pouch' : ['flint', 'twine', 'gemstone'],
#     'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
# }
# inventory.setdefault('pocket',['seashell','strage berry','lint'])
# inventory['backpack']=sorted(inventory['backpack'])
# print(inventory)
# inventory['backpack'].remove('dagger')
# print(inventory)
# inventory['gold']+=50
# print(inventory)

# *************Question 6 *********************
# . Folow the steps bellow: -Create a new dictionary called prices using {} format like the example above.
# •	Put these values in your prices dictionary:
# •	"banana": 4,
# •	"apple": 2,
# •	"orange": 1.5,
# •	"pear": 3
# •	Loop through each key in prices. For each key, print out the key along with its price and stock information. Print the answer in the following format:
# •	apple
# •	price: 2
# •	stock: 0
# •	Let's determine how much money you would make if you sold all of your food.
# o	Create a variable called total and set it to zero.
# o	Loop through the prices dictionaries.For each key in prices, multiply the number in prices by the number in stock. Print that value into the console and then add it to total.
# o	Finally, outside your loop, print total.

# prices={'banana':4,'apple':2,"orange":1.5,'pear':3}
# stock={'banana':6,'apple':0,'orange':32,'pear':15}
# s=0
# for i in prices:
#     s=s+(prices[i] * stock[i])
#     print(f"{i}\nPrice: {prices[i]}\nStock: {stock[i]}")
#     print(f"price × stock: {prices[i]}×{stock[i]} = {prices[i] * stock[i]}\n")
# print(f"Money from selling everything: {s}")

# ***************Question 7 ********************
# Follow the steps:
# •	First, make a list called groceries with the values "banana","orange", and "apple".
# •	Define this two dictionaries:
# stock = {
#     "banana": 6,
#     "apple": 0,
#     "orange": 32,
#     "pear": 15
# }

# prices = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }
# •	Define a function compute_bill that takes one argument food as input. In the function, create a variable total with an initial value of zero.For each item in the food list, add the price of that item to total. Finally, return the total. Ignore whether or not the item you're billing for is in stock.Note that your function should work for any food list.
# •	Make the following changes to your compute_bill function:
# o	While you loop through each item of food, only add the price of the item to total if the item's stock count is greater than zero.
# o	If the item is in stock and after you add the price to the total, subtract one from the item's stock count.

# def compute_bill(food):
#     total=0
#     for i in food:
#         if(stock[i]>0):
#             stock[i]-=1
#             total=total+prices[i]
#     return total

# groceries=['banana','orange','apple']
# stock = {"banana": 6,"apple": 0,"orange": 32,"pear": 15}
# prices = {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}

# k=compute_bill(groceries)
# print(k)

# ***************Question 8 ****************
# This exercise is a bit more complicate. We will review all about list and dictionaries. The aim of this exercise is to make a gradebook for teacher's students.
# Try to follow the steps:
# •	Create three dictionaries: lloyd, alice, and tyler.
# •	Give each dictionary the keys "name", "homework", "quizzes", and "tests".Have the "name" key be the name of the student (that is, lloyd's name should be "Lloyd") and the other keys should be an empty list. Look in solutions, the "solution 1". Chechk if you have done it rigth.
# •	Now copy this code:
# •	lloyd = {
# •	  "name": "Lloyd",
# •	  "homework": [90.0,97.0,75.0,92.0],
# •	  "quizzes": [88.0,40.0,94.0],
# •	  "tests": [75.0,90.0]
# •	}
# •	alice = {
# •	  "name": "Alice",
# •	  "homework": [100.0, 92.0, 98.0, 100.0],
# •	  "quizzes": [82.0, 83.0, 91.0],
# •	  "tests": [89.0, 97.0]
# •	}
# •	tyler = {
# •	  "name": "Tyler",
# •	  "homework": [0.0, 87.0, 75.0, 22.0],
# •	  "quizzes": [0.0, 75.0, 78.0],
# •	  "tests": [100.0, 100.0]
# •	}
# •	Below your code, create a list called studentsthat contains lloyd, alice, and `tyler.
# •	for each student in your students list, print out that student's data, as follows:
# o	print the student's name
# o	print the student's homework
# o	print the student's quizzes
# o	print the student's tests
# •	Write a function average that takes a list of numbers and returns the average.
# o	Define a function called average that has one argument, numbers.
# o	Inside that function, call the built-in sum() function with the numbers list as a parameter. Store the result in a variable called total.
# o	Use float() to convert total and store the result in total.
# o	Divide total by the length of the numbers list. Use the built-in len() function to calculate that.
# o	Return that result.
# •	Write a function called get_average that takes a student dictionary (like lloyd, alice, or tyler) as input and returns his/her weighted average.
# o	Define a function called get_average that takes one argument called student.
# o	Make a variable homework that stores the average() of student["homework"].
# o	Repeat step 2 for "quizzes" and "tests".
# o	Multiply the 3 averages by their weights and return the sum of those three. Homework is 10%, quizzes are 30% and tests are 60%.
# •	Define a new function called get_letter_grade that has one argument called score. Expect score to be a number.
# o	Inside your function, test score using a chain of if: / elif: / else: statements, like so:
# o	If score is 90 or above: return "A"
# o	Else if score is 80 or above: return "B"
# o	Else if score is 70 or above: return "C"
# o	Else if score is 60 or above: return "D"
# o	Otherwise: return "F"
# o	Finally, test your function. Call your get_letter_grade function with the result of get_average(lloyd). Print the resulting letter grade.
# •	Define a function called get_class_average that has one argument, students. You can expect students to be a list containing your three students.
# o	First, make an empty list called results.
# o	For each student item in the class list, calculate get_average(student) and then call results.append() with that result.
# o	Finally, return the result of calling average() with results.
# •	Finally, print out the result of calling get_class_averagewith your students list. Your students should be [lloyd, alice, tyler].
# •	Then, print the result of get_letter_grade for the class's average.

def average(lis):
    s=0
    s=sum(lis)
    return s/len(lis)
def get_average(dic):
    l = ['homework', 'quizzes', 'tests']
    weights = [0.10, 0.30, 0.60]
    total = 0
    for i in range(len(l)):
        av = average(dic[l[i]])
        total = total + av * weights[i]
    return total
def get_letter_grade(score):
    if isinstance(score, dict):
        sc=get_average(score)
    else:
        sc=score
    if(sc>=90):
        return 'A'
    elif(sc>=80 and sc<=89):
        return 'B'
    elif(sc>=70 and sc<=79):
        return 'C'
    elif(sc>=60 and sc<=69):
        return 'D'
    else:
        return 'F'

def get_class_average(stu):
    result=[]
    for i in stu:
        get=get_average(i)
        result.append(get)
    avg=0
    avg=sum(result)/len(result)
    return avg
lloyd = {"name": "Lloyd","homework": [90.0,97.0,75.0,92.0],"quizzes": [88.0,40.0,94.0],"tests": [75.0,90.0]}
alice = {"name": "Alice","homework": [100.0, 92.0, 98.0, 100.0],"quizzes": [82.0, 83.0, 91.0],"tests": [89.0, 97.0]}
tyler = {"name": "Tyler","homework": [0.0, 87.0, 75.0, 22.0],"quizzes": [0.0, 75.0, 78.0],"tests": [100.0, 100.0]}
students=[lloyd,alice,tyler]
for v in students:
    print(f"Name: {v['name']}\nHomework: {v['homework']}\nQuizzes: {v['quizzes']}\nTests: {v['tests']}\n")
k=get_class_average(students)
k1=get_letter_grade(k)
print(f"Class average: {k}")
print(f"Class Grade: {k1}")