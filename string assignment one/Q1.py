# ******Question 1 *******
# Count how many of each vowel (a,e,i,o,u) there in a text string, and print, and the count for each vowel with a single formate string. Remember that vowels can be both lower and uppercase.
# x=input("Enter string: ")
# i=x.upper()
# for v in "AEIOU":
#     c=i.count(v)
#     print(v,"=",c)

# *******Question 2**********
# Below is a text with several characters enclosed in square brackets [ and ].
# Scan the text and print out all characters which are between square brackets.

# t  =	"""And  sending	tinted  postcards  of  places  they  don ' t
# realise  they  haven ' t	even	visited  to	' All  at  nu[m]ber  22,  weather
# w[on]derful ,  our	room	is	marked  with	an	' X ' .  Wish  you  were  here.
# Food  very  greasy	but  we ' ve  found  a  charming  li[t]tle  local  place
# hidden	awa[y  ]in	the  back  streets  where  they  serve  Watney ' s  Red
# Barrel	and  cheese	and	onion  cris[p]s	and	the  accordionist  pla[y]s
# "Maybe	i[t ] ' s  because	I ' m  a  Londoner " '  and  spending  four  days  on
# the  tarmac  at  Luton  airport  on  a  five -day  package  tour  wit[h]
# n[o]thing  to  eat	but	dried  Watney ' s	sa[n]dwiches ... """

# i=0
# while(True):
#     i=t.find('[',i)
#     y=t.find(']',i+1)
#     if(i==-1):break
#     print(t[i+1:y],end='')
#     i=i+1

# *******Question 3*********
# Print a line of all the capital letters "A" to "Z". Below it, print a line of the letters that are 13 positions in the alphabet away from the letters that are above them. E.g., below the "A" you print an "N", below the "B" you print an "O", etcetera. You have to consider the alphabet to be circular, i.e., after the "Z", it loops back to the "A" again.
# i=65
# while(i<=90):
#     print(chr(i),end='')
#     i+=1
# print()
# i=78
# while(i<=90):
#     print(chr(i),end='')
#     i+=1
# i=65
# while(i<78):
#     print(chr(i),end='')
#     i+=1

# **********Question 4********
# In the text below, count how often the word “wood” occurs (using pro-gram code, of course). Capitals and lower case letters may both be used, and you have to consider that the word “wood” should be a separate word, and not part of another word. Hint: If you did the exercises from this chapter, you already developed a function that “cleans” a text. Combining that function with the split() function more or less solves the problem for you.
# text = "How much wood would a woodchuck chuck If a woodchuck could chuck wood? He would chuck, he would, as much as he could, And chuck as much as a woodchuck would If a woodchuck could chuck wood."
# i=text.upper()
# r=i.replace(".","")
# r=r.replace("?","")
# j=r.split(' ')
# i=0
# c=0
# while(i<len(j)):
#     if(j[i]=='WOOD'):
#         c+=1
#     i+=1
# print(c)

# ***********Question 5******
# Write a program that takes a string and produces a new string that con-tains the exact characters that the first string contains, but in order of their ASCII-codes. For instance, the string "Hello, world!" should be turned into " !,Hdellloorw". This is relatively easy to do with list functions, which will be introduced in a future chapter, but for now try to do it with string manipulation functions alone.
# x=input("Enter string:")
# t=sorted(x)
# print("".join(t))

# *********Question 6********
# Typical autocorrect functions are the following: (1) if a word starts with two capitals, followed 
# by a lower-case letter, the second capital is made lower case; (2) if a sentence contains a word that
#  is immediately followed by the same word, the second occurrence is removed; (3) if a sentence starts
# with a lower-case letter, that letter is turned into a capital; (4) if a word consists entirely of 
# capitals, except for the first letter which is lower case, then the case of the letters in the word 
# is reversed; and (5) if the sentence contains the name of a day (in English) which does not start with
#  a capital, the first letter is turned into a capital. Write a program that takes a sentence and makes these 
#  auto-corrections. Test it out on the string below.

# (1) if a word starts with two capitals, followed by a lower-case letter, the second capital is made lower case;

# x = "SUnday"
# if (x[0].isupper() and x[1].isupper() and x[2].islower()):
#     x = x[0] + x[1].lower() + x[2:]
# print(x)

# (2) if a sentence contains a word that is immediately followed by the same word, the second occurrence is removed;
# x = "as it turned out our aRTHUR BElling was was to change every sunday we ' d hurry along to and Jam ..."

# x="Hello world world how are are you"
# x=x.split(" ")
# i=0
# t=''
# while(i<len(x)-1):
#     if(x[i]!=x[i+1]):
#         t=t+x[i]+" "
#     i+=1
# t=t+x[i]
# print(t)

# (3) if a sentence starts with a lower-case letter, that letter is turned into a capital; 
# x = "as it turned out our aRTHUR BElling was was to change every sunday we ' d hurry along to and Jam ..."

# x=input("Enter string:")
# t=x.capitalize()
# print(t)


# ***(4) if a word consists entirely of capitals, except for the first letter which is lower case, then the case of the letters in the word is reversed

# x = "as it turned out our aRTHUR BElling was was to change every sunday we ' d hurry along to and Jam ..."

# x="aRTHUR"
# t=''
# for i in x:
#     if(i.islower()):
#         i=i.upper()
#     else:
#         i=i.lower()
#     t=t+i
# print(t)

#(5) if the sentence contains the name of a day (in English) which does not start with a capital, the first letter is turned into a capital. 
# u = "as it turned out our aRTHUR BElling was was to change every sunday we ' d hurry along to and Jam ..."

# u="Hello today is sunday"
# x=u.split(" ")
# t=''
# i=0
# while(i<len(x)):
#     for w in ["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]:
#         if(x[i]== w):
#             x[i]=x[i].capitalize()
#     i+=1

# print(" ".join(x))

# sentence = "as it turned out our aRTHUR BElling was was to change every sunday we ' d hurry along to and Jam ..."


