# 15-11-24 #Day 1 - Basic into. about python
# commet
# sinle line commet [ctrl+/] - code will not execute

#Q. what is Python?*
# = it is general purpose high level programming language. established in 1989 by Guido van rossam.(1991 for public)

#Q. where it is used?*
# = to make desktop application, web application, networke programing, database,game development, ai

#Q. feature of phyton?**
# = simple and easy to learn[simple:sintex(compare to java),freeware and open_source(free for ous or without licence),
# high level programming language(handle low level task;memory manage:- pvm, garbage collection),
# dynamic language(do not need to explain steps),
# support both Object(oop) And Procedure oriented language(step by step)]

# garbage collection eg =
# a=10
# a=20
# print(a) =  #it will print latest, because it will consider the latest value and rest it will delete.

# ------------------------------------------------------------------------------------------------------------------------

# 18-11-24 day 2 - Identifier
# = a name in a python is called a identifier
#  module* - is a file name of a pyhton file

#  variable* - is  a something where we can put
# eg -

# function name* - is made using Def keyword
# eg - def saransh()

# class name* - it define using call keyword
# eg - class saransh()

# Pyhton as two function :
# user define function- we need to use #Def key word
# built in function- function which are build in.

# 1st rule of Module :- Satrts with Alphabate : a, A (cannot start with Digits)
# eg- a= 10 (correct)
# 2= 123(incorrect)

# 2nd rule :- no spacial character are allowed (only underscore are allowed):
# eg- a#b = 10 (incorrect)
# a_b=10 (correct)

# 3rd rule :- Private variable - starts with single Underscore
# eg- _a=10
# def _Saransh() (private variable)
# class _Mrunmayee() (private variable)
# - Strongly variable - starts with double underscore
# eg- __a=10
# def __saransh (strongly variable)

# 4th :- Python is a case sensitive language
# eg- a=10
# A=10

# 5th rule :- Keywords/Reserved name cannot used -

# -----------------------------------------------------------------------------------------------------------------------

# 19-11-24 Day 3 - Reserved words(keywords) [35]
# in python some words are reserved with specific functionality which is in-build in python keyword.

# import keyword [form & import are use to call]
# d=keyword.kwlist (keyword=module name) (kwlist=)
# print(d)

# 'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
# 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
# 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# -----------------------------------------------------------------------------------------------------------------------

# Datatype [14]
# = datatype represent the type of data present inside the variable. eg- print(type(s))

# 1> int(integers)- any number
# a = 20
# print(type(a))* =======> this is how we check datatype. i.e= (int)

# 2> float - any value/no. present in dot
# eg- 10.3, 9.8, 3.7

# 3> bool(boolian) - any datatype comes in true & false [true=1(non-zero); false=0]

# 4> str (string)
# Q. what is string?
# = any data which is inside or enclosed single / double cote (''/ " ")

# 5> complex - it is of two type, i.e .real and imaginary'. it is in 'i and j'
# eg- s=3+5j  ('j' is only nessarry) [where 3 is real & 5j is imaginary]
# print(s.real) =====> outcome- 3
# print(s.imag) =====> outcome- 5

# ABOVE 5 DATATYPES  ARE FUNDAMENTAL DATATYPE. (i.e- int, float, bool, str, complex)

# -----------------------------------------------------------------------------------------------------------------------

# 20-11-2024
# multiple line string :- we have to give Triple double/ Triple single cote

 # eg- s= """ i
 # love
 # rcb """

# multiple line comment :- under triple double cote
"""
eg :- s=10
a=5
print(a)
"""

# Q.> How memory manage in python? =====> Memory manage in python by python heap space memory.***
#= Two type of memory
# 1> Stack memory = store variable , eg- a= ; b=

# 2>Heap space memory = store Value , =10; ="saransh"

#  id
# a=10
# b=10
# c=10
# d=20
# e=20
# f=50
# g=51
# # stack memory = a,b,c,d,e
# # heap space memory = 10,20 [any duplicate value will store once]
#
# print(id(a))  =========> in-build code to know about id
# print(id(b))
# print(id(c))
# print(id(d))
# print(id(e))
# print(id(f))
# print(id(g))
# print(id(a))
# EVERYTHING IN PYTHON IS A 'OBJECTS' ***
# ALL FUNDAMENTAL DATA TYPE IS IMMUTABLE [(IMMUTABLE= no changeable behaviour)& (MUTABLE= changeable behaviour)]***

# 21-11-2024
# type casting
# = when we convert one data type to another data type.
# eg-
# s=10    int changes to remaining fundamental DT.
# s1=bool(s)
# print(s1)
# s2=str(s)
# print(s2)
# s3=float(s)
# print(s3)
# s4=complex(s)
# print(s4) =======>10+0j (outcome)

# *** STR(string) datatype cannot convert into another datatype except it's a base 10 value ***

# ------------------------------------------------------------------------------------------------------------------------

# 25-11-25 #Data Types (remaining 6-14)

# 6> list
# l=[1,2,'mrunmayee',True]    #hetrogeneous:- a, comma-separated
# l2=[]
# l3=[1,2,3,4]
# print(type(l))
# print(type(l2))
# print(type(l3))


#Q. difference between list and tuple
# List is enclosed with square bracket
# Tuple is enclosed with round bracket ; Comma is mandatory eg (1,)

# 7> tuple
# t = (1, 1.2, "K")
# t1 = (1,2,3,4)
# t2 =(1,) #If I don't give comma it will be integer/string/float*
# t3 =(1)
# print(type(t))
# print(type(t1))
# print(type(t2))
# print(type(t3))

# 8>SET  enclosed with curly braces {}
# s = {1,2,3,4,4} #duplicated not allowed, same values will not be printed
# print(type(s))
# print(s)

# 9>frozenset
# s=frozenset[1,2,3,4] #immutable
# print(type(s))
# print(s)

# 10>range: # type--integer used --used mainly in for loop, number -1 : (1,10) ---> 1,2,3,4,5,6,7,8,9;;
# for i in range(5):
#     print(i) ======>   #0,1,2,3,4

# r= range(5)
# # print(list(r))  =====> #[0, 1, 2, 3, 4]
# print(tuple(r))   =====> #(0, 1, 2, 3, 4)

# 2 (10) 0,1,2,3,4,5,6,7,8,9
# 3
# range(2, 21, 2) ------>(2,4,6,8,10....)
# range (2,21,3)  ------>(2,5,8,11,14,18)
# print(range)

# 11> Bytes #immutable
# b= bytes

# 12> Bytearry
# x=[1,2,3,4]
# b=bytearray(x)
#     for i in b:
#     print(i)

#array --------> not included in 14 datatypes **
#same data type in list is array s=[1,2,3,4]

# 13> Dictionary {key:value}
# d={"a":2,"b":4}
# print(type(d))

# 14> None -----> none means none data type

# ------------------------------------------------------------------------------------------------------------------------

# 26-11-24
# list, tuple, set, dict, string
# indenting slicing [in set data type indenting & slicing does not work]
# operator (symbole i.e- +,-,*)
# input eval
# flow control
#
#
# operator :-  Is a symbol that perform some operations. symbole [+,-, *, /, //(floor division),**(exponent opt/power opt)
# %(modulo opt)]

# -----------------------------------------------------------------------------------------------------------------------

# OPERATOR - it is just a symboles

# A>. arithmatic opt :-([+,-, *, /, //(floor division),**(exponent opt/power opt) %(modulo opt), ]

# eg :
# + (addition)
# a=10
# b=20
# c=(a+b)
# print(c)

#  + addition (int) , concatination :- Both oprants/data should be "String"**
# (1+2) 1= 1st oprants; 2= 2nd oprants
# in addition Both Oprants Should be interger
# s= 1+2
# print(s)-----> it will print
#
# s= 1+ "saransh"
# print(s)-----> it will show type error


# s= "saransh" + "wawre"
# print(s)-----> it will print o/p(saranshwawre)

# *(multiplication), repeat
# a=10
# b=20
# c=(a*b)
# print(c)

# /(division)
# a=10
# b=5
# c=(a/b)
# print(c)

# / (division)
# a=10
# b=5
# c=(a/b)
# print(c)  #------> o/t will be float value

# // (floor division)
# a=10
# b=5
# c=(a//b)
# print(c)

# ** (exponent opt/power opt)
# print(2**4) #------> o/p 16
# print(3**2) #------>9

# % (modulo) *Remaning value will show
# a= 10
# b= 3    #(a mod of b)
# c= (a%b)
# print(c) #-----> 1 *Remaning value will show
# note:- output will depend on data inputs. in floor division o/p will be integer/float depends on input
# Q> different between single slash and double slash?**
# =>

# * repetation opt (integer is required)

# 1> multiplication
# eg
# a=2
# b=4
# print(a*b) ------> p/t= 8

# 2> to combine

# a=2
# b="saransh"
# print(a*b) -------> saranshsaransh
#
# a="saransh"
# b="wawre"
# print(a*b) ------> type error ()

# 27-11-24

# relation operation :- ( > ,>=, <, <=) o/p boole* i.e true & false
# s=20
# g=20
# print(s>=g)
#
# a=20
# b=10
# print(a<=b)
#
# e=400
# f=20
# print(e>f)
#
# c=30
# d=20
# print(c<d)

# Order(ORD) :
# - its a inbuild function where, "Upper case is 'smaller' & Lower case is 'bigger'."
# y="a"
# z="a"
# print(y>z) #======>false
#
# y="a"
# z="A"
# print(y>z) #=======>true
# print(ord("a"))
# print(ord('A'))

# Indentation :- how to write a code in python


# B>. logical opt
# 'and','or','not'
# 'and' = 'to check two or more condition'
# eg:-
# condition1 and condition2 ===> if condition match the o/t= True
# TT = T
# TF = F
# FT = F
# FF = F
# eg:-
# a=10
# b=20
# c=30
# d=40
# print(a<b and c>d)

# 'or' =
# TT = T
# TF = T
# FT = T
# FF = F
# eg:-
# a=10
# b=20
# c=30
# d=40
# print(a<b or c<d)

# 'not' = revers the result
# eg:-
# a=10
# b=20
# c=(b>a)
# d= not (b>a)
# print(c)
# print(d)


# C>. membership opt (in, not in)
#
# s="family"
# print("f" in s) #True
# print("i" in s) #True
# print("s" in s) #False, because 's' is not member of "family"
# print("s" not in s) #True, because 'not in' will reverse the o/p.
# print("im" in s) #False , because the sequence is from left to right

# D>. idetify opt (is, is not)
# it will match the 'id'** & data type Immutable*
# eg:-
# s=10
# s1=10
# print(id(s)) #140719011062984
# print(id(s1)) #140719011062984
# print(s is s1) #True
# #  mutable & immutable
# s=[1,2]
# s1=[1,2]
# print(id(s)) #2013338051264
# print(id(s1)) #2013337903296
# print(s is s1) #False
#
# s=("saransh")
# s1=("saransh")
# print(id(s))
# print(id(s1))
# print(s is s1)
#
# s={"saransh"}
# s1={"saransh"}
# print(id(s))
# print(id(s1))
# print(s is s1)

# E>. eqaulity opt
# Q>. difference between single equal to '=' and double equal too'=='
# ans> "=" is a assigment opt ; "==" matches the value
# double equal too (==)
# eg:-
# a=10
# b=10
# print(a==b)
# a=10
# b=100
# print(a!=b)
# when both value are equal then it will 'true' else it will 'false'

# not equal too (!=)


# F>. ternory opt**
# Q> what is Syntex of ternory opt?***
# ans>  s= exp1 if 20>10 else exp2
#                     <==true
# s= "firstvalue" if "condition" else "secondvalue"
#                      false==>
#
# if= 'jar'                      else= 'nahi tar'
# a="saransh" if 20>10 else "mrunmayee"
# print(a)

# a,b=10,20
# print(a) ===>10

# a,b=10,20
# print(c) #===> error 'not enough values to unpack (expected 3, got 2)'
# x= "saransh" if b<a else "mrunmayee"
# print(x)

# a=10
# b=50
# c=30
# d=60
# max= a if a>b and a>c else b if b>c and b>d else c if c>d  else d
# print(max)

# Operator

# Assigment opt
# a=10
# a+=5
# print(a)
# ----------------------------***********------*********-------*******-----------------------------------------------------

# Input-Output and eval

# we fill some Form (name, address, ph.no., email)
# when we integrate/ connect code with jango using input function from user.not
#.> Input() function can be use to read the data directly from the user
#.> Output () function is a print statement
#.> Eval() function:- when we have to take data inpt in list,tuple,set datatype

# input()*
# a=input('enter your first value :')
# b=input('enter your second value:')
# print (a+b) #o/p will give as concatenation as the value is 'string'
# c=int(a) # by using type casting
# d=int(b)
# print(c+d)

# a = int(input('enter your first value:'))
# b = int(input('enter your second value:'))
# print(a+b)

# Eval()*
# #.> Eval() function:- when we have to take data inpt in list,tuple,set datatype
# eval() function take 'string' and evaluates the data
# eg-
# s=eval('10+2+3') #math function bhi print kr skte hai
# print(s)

# s=eval(input("enter list:"))
# print(s)
# o/p:-enter list:[1,2,3]
# [1, 2, 3]

# -----------------------------------------------------------------------------------------------------------------------

# FLOW CONTROL
# python supports to 'oops concepts' and 'procedure oriented'(line by line code )
# flow control will 'describe the order in which the statement will be execute at runtime'.

# statement 1> Conditional statement - (if, elif, else)
# statement 2> Transfer statement - (break, continue, pass)
# statement 3> Iterative statement[loop] - (for,while)

# eg:-
# a=20
# b=30
# if b<a:
#     print("saransh")
# else:
#     print("kuki")
#   it will print line '517' and do not print line'515' because we use condition statement

# Condition statement - (if, elif,else)

# if condition:
#     print("action1")
# elif condition2 and more:
#     print("action2")
# else:
#     print("action3")
# eg-
# a=10
# b=20
# if a>b:
#     print('saransh')
#     print('wawre')
# elif a==b:
#     print("mrunmayee")
# elif a<b:
#     print("sarmayee")
# else:
#     print("kuki")

# akash="nike"
# saransh="add"
# nikhil="puma"
# mrunmayee="zara"
# dhawal="roadstar"
# mrunal="except top 5"

# brand = input('enter the brand name:')
# if brand == 'nike':
#     print('akash')
# elif brand == 'add':
#     print('saransh')
# elif brand == 'puma':
#     print('nikhil')
# elif brand == 'zara':
#     print('mrunmayee')
# elif brand == 'roadstar':
#     print('dhawal')
# else :
#     print('mrunal')

# TO find out the lowest value
# v1=input('enter your value 1:')
# v2=input('enter your value 2:')
# v3=input('enter your value 3:')

#NESTETIF
    # a=10
    # b=20
    # c=30
    # if b>a:
    #     if a>c:  #nestetif
    #         print('abcd')
    #     else:
    #         print('xyz')
    # else:
    #     print('123')

# Iterative stat
# Q> what is itrative and iterable
# ==> in iterative there are Two type of loop [for loop and while loop]
    # = if we want to exective a group of statement multiple time called as Iteraative.
# (transversal=it will check for every element)

# *for loop= if we want to exective some action/condition for every element present in sequence(i.e- string or collection)
# collection = list, tuple, dist
# sequenc =intrative
# pratak element vr datatype lavta yenr
# eg (for)
# s='saransh' #string
# for k in s:
#     print(k)
# # O/p- s,a,r,a,n,s,h is "iterable"**
# s1=(1,2,3,4) #list
# s2=(1,2,3,4,5) #truple


# for iin range(5):
#     print(i) #o/p=0,1,2,3,4
#     print("hey")
# #o/p=hey,hey,hey,hey,hey

# *while loop= untile the code is true, the code will run (in infinity) and if condition will false it will stop
# = if we want to execute a group of stat until some condition false, then we should go for 'while loop'.
# while condition : infinity
# code : executive

# eg:
# x=1
# while x<=10:  #condition i.e True
#     print(x)  #
#     x=x+2

# eg for practice
# v=input('enter your name:')
# while v != "python" :
#     print(v)
# print('1234')

# Transfer Condition (key word: break, continue, pass)
# Q> what pass do?

# break* = it will stop the loop, based on the condition.
# eg
# s=[1,2,3,4,5,6,7,8]
# for i in s:
#     if i == 4:
#         break
#     print(i)

# a= 'saransh'
# for i in a:
#     if i == 'r':
#         break
#     print(i)

# continue* = condition will skip
# eg
# s=[1,2,3,4,5,6,7,8]
# for i in s:
#     if i == 4:
#         continue
#     print(i)

# pass* = its a keyword in python, it has nothing to do.
# eg
# a=100
# b=20
# if a>b:
#     pass

# ---------------------------------------------------------------------------------------------------------------------
# Indexing & slicing

# Slicing : if we want a data in type.
# (s[start:end+1:step]) (step= )
# by default [0:total length:1]
# s="saransh dewanand wawre"
# print(s[0:7]) #o/p= saransh
# print(s[0:7:3])
# print(s[8:16])
# a='01234567'
# print(a[1:7:4])
# print(a[::])
# Indexing :
# forward indexing(positive) : travel left to right, and starts with zero'0' and increase by '1'
# s="saransh dewanand wawre"
# print(s[0]) #o/p= s

# revers indexing(negative) : travel right to left, starts with '-1' and increase by '1'
# s="saransh dewanand wawre"
# print(s[-1])


# ---------------------------------------------------------------------------------------------------------------------

# String data type :

# string - any data which is inside or enclosed single / double cote (''/ " ")
#  s= 'dolly's chai wala'      invalid
# s1 = "dolly's chai wala"     valid
# s2 = 'dollys chaiwala/'s '   valid (forward /)
# s3 =  'this"abc is a python class'    valid

# Q. How to access character from string?
# => by using 'indexing and slicing'

# =====================================================================================================================
# STRING***

# Strip() [spaces]


# a = "  sir is a django developer   "
# backend developer have to remove the extra space
# strip()* =====> it will remove the spaces
#
# lstrip() ===> it will remove left strip/space
# rstrip() ===> it will remove right strip/space
# print(a)
# print(a.strip())  #both side space will remove
# print(a.rstrip())
# print(a.lstrip())

# "    nagpur "
# "   nag pur " # space : invalid by membership op
# "  nagpur    " #remove

# Finding The Substring:
# => anything inside the string is  a substring
# m= "123python developer, 123python developer"
# 1>. find() :- it will use the starting index no, o/p = 3
# If there is no substring in the string o/p = -1
# eg:-
# print(m.find("python")) #o/p=3
# print(m.find("java")) #o/p= -1

# Index:-
# Q> Difference between find and index ?
# => index() :- it will show the value error.
# print(m.index("python"))
# print(m.index("java"))

# rfind:- it will search the revers way i.e right to left, But it count in forward way.
# print(m.rfind("python")) #o/p=24
# print(m.rindex("python"))
#
# find = -1
# index = error

# s="pythondeveloper"
# print(s.find("dev")) #o/p=6
# print(s.find("dev",0,9)) #o/p=6
# print(s.find("dev",0,7)) #o/p=-1
#
#
# # count():- it will count in main string that how many searched string is there.
# M="pythondeveloperpythondeveloperpythondeveloper"

# Replace

# m='python developer' #as it is a string and its a immutable
# m1=m.replace('python','java')
# print(m1)
#
# s="waah waah waah waah"
# s1=s.replace('waah','yeah')
# print(s1)

# Q. how you can change string(immutable) data type
# = by taking another variable

#Join
# = to join the string (tuple or list), by default it is coma seperated

# m=("saransh","mrunmayee")
# m1="+".join(m)
# print(m1) #o/p saransh+mrunmayee

# Changing Case of the string***
# = to change improper to proper data

# name:saRAnsh   lastname:waWRe
# Saransh wawre
# eg:
# s="PyThon DevELoper"
# 1. upper() : PYTHON DEVELOPER
# 2.lower() : python developere
# 3.swapcase() : [change lower to upper and upper to lower ] : pYthON dEVelOPER
# 4.title() : [first letter will be capital of every character] : Python Developer
# 5.capitalize() : [first word of 1st character will be Capital] : Python developer

# print(s.upper())
# print(s.lower())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())


# Startswith and Endswith

# s="saransh is a python developer"
# print(s.startswith("saransh")) #o/p True
# print(s.startswith("mrunmayee")) #o/p false
#
# print(s.endswith("python")) #o/p False
# print(s.endswith("r"))#o/p True
# print(s.endswith("developer")) #o/p True


# To Check the Type of Character present in 'string'

# 1. isalnum : [a-z; A-Z; 0-9]
# 2. isalpha : [a-z: A-Z]
# 3. isdigit : [0-9] (only digit)
# 4. islower : [a-z] (all character are in lower case)
# 5. isupper : [A-Z] (all character are in upper case)
# 6. istitle : [first letter will be capital of every character]
# 7. isspace : [space is need in a string]

#======================================================================================================================
# FORMATING
# to print a string in particular format, '{}' is used.
# formate{}


# name=("saransh")
# age=24
# Without formating
# print("my name is",name," and my age is ",age)
# using formating
# 1> print("my name is {} and my age is {}".format(name,age))

# 2> print("my name is {0} and my age is {1}".format(name,age))
# print("my name is {1} and my age is {1}".format(name,age))
# print("my name is {0} and my age is {0}".format(name,age))

#3> print("my name is {n} and my age is {a}".format(n=name,a=age))

#4> s=f"my name is {name}, and my age is {age}"
# print(s)

# ====================================================================================================================
# List : []***

# when to use list? ==> when we want single entity we want multipal datatype.(hetrogenious data)
# value seperated by coma
# duplicate data allowed
# insertion order is preserved(duplicate value has different index no.)
# it is dynamic/mutable
# indexing and slicing applicable

# when to use list?
# ==> if we want to represent a group of individual object in a singlle entity, where insertion order is preserved.

# Q>how to creat list?
# 1> empty
# a=[]
#
# 2>with value?
# a1=[1,2,3,4,5]
#
# 3>using eval
# s=eval(input("enter ur list data"))
# print(s)
# print(s[2])

# 4> using range datatype with list function
# s=list(range(2,21,2))
# print(s)

# 5> Split : strint DT split Conversion list
# s="python developer from Uganda"
# m=s.split()
# print(m)

# Mutable
# Replace the value of particular index no.
# s=[1,2,3,4,5]
# print(s)
# print(s[1])
# s[1]=200
# print(s)
# s[4]=69
# print(s)

#length()
# s=[1,2,3,4]
# print(len(s))

#count()
# s=[1,2,3,4,5,6,1,2,3,4,5,5,6,7,8,9]
# print(s.count(9))

#index()
# s=[1,2,3,3,2,1]
# print(s.index(3))

#append()
# to add the element in the end of the list.
# s=[]
# s.append(1)
# s.append(9)
# s.append("hello")
# a.append(10,20,30) #error because of multiple element
# print(s)

# a=[10,20]
# a.append(1)
# a.append(10)
# print(a)

# s="saransh12345"
# s1=[]
# for i in s:
#     if i.isdigit():
#         s1.append(i)
# print(s1)

#insert()
# to insert the element at specific index number.
# Q.> what insert() do?
# s=[1,2,3]
# s.insert(1,200)
# s.insert(5,500) #max index is 2, but we consider 5 so it will print at end
# s.insert(-10,900)
# print(s)

# Extend()
# to add all items from one list to another. i.e 2 list are compulsory
# m1=[1,2,3]
# m2=[9,8,7]
#
# m2.extend(m1)
# print(m2)

# s1=["saransh","mrunmayee","nikhil"]
# s2=["mrunal"]
# s1.extend(s2)
# print(s1)

# Remove()
# it will remove the specific index no. i.e first occurance
# s=[1,2,3,4,5,1,2]
# s.remove(1)
# print(s)

# Pop()
# it will remove and return the end value of the list[], and show on the o/p
# s=[1,2,3,4,5]
# print(s.pop())  #o/p= 5
# print(s) #o/p=[1,2,3,4]
# print(s.pop())
# print(s)
# s=[]
# print(s.pop()) #o/p=error

# Q.> What is the different between remove and pop?

#LIFO (last in first out)
# s=[1,2,3,4]
# print(s.pop(1))
# print(s)

# extend: extend(); insert(); append()
# remove: remove(); pop()

#Reverse()
# it will revers the element
# s=[4,5,3,2,1]
# s.reverse() #it apply on every element, it
# print(s)

#Sort()
# s=[1,26,3,45,5]
# s.sort()
# print(s) #o/p assending order
#
# s1=[1,26,3,45,5]
# s1.sort()
# s1.reverse()
# print(s1) #o/p decending oreder
#
# m=[1,23,45,67,33,1]
# m.sort()
# print(m)

# u=('saransh','mrunmayee','virat','Saransh')
# u1=list(u)
# print(u1)
# u1.sort()
# print(u1)

# s=[4,2,3,1]
# s.sort(reverse=True)
# print(s)

# =====================================================================================================================
# nested list ===> list under list
# s=[1,2,3,[4,5,6],7,(8,9,0)]
# print(s[3]) #o/p=[4,5,6]
# print(s[3][1]) #o/p=5
# print(s[5]) #o/p= (8,9,0)

# Aliasing and Cloning***

#Aliasing
# the process of giving another refrance variable to the existing list.
# a= [1,2,3]
# b=a  # aliasing: 'b' refers to the same list as 'a'
# # print(a)
# # print(b)
# # print(id(a))
# # print(id(b))
#
# b[1]=69
# print(a) #o/p= [1,69,3]

#Cloning
# a=[1,2,3]
# b=a[:]
# a[1]=69
# print(a)
# print(b)

# comparision
# (==; !=)
# 1> no. of element present inside the list
# 2> Order of the element
# 3> The content of element(ie. uppeer case/lower case)

# x=["saransh","nikhil","mrunmayee"]
# y=["saransh","nikhil","mrunmayee"]
# print(x==y)

# (<; >; <=; >=)
# 1>Only 1st element get compared
# s=[30,40,50]
# s1=[10,20,30,400,600,789]
# print(s>s1)

# Clear()
# d=[1,2,3]
# d.clear()
# print(d)

# List comprehension***
# comprehension ==> single line code
#
# s=[]
# for i in range(1,11):
#     s.append(i)
# print(s)
#
# a=print([output for output in range(1,11)])   #list comprehension of above code

# m=print([output*2 for output in range (1,6)]) #o/p=[2, 4, 6, 8, 10]

# exp , for
# # eg= [exp for i in range(1,6)]
#
# exp, for, if
# s=[1,2,3,4,5,6,7,8]
# s1=print([x for x in range(10) if x%2==0])
#
# exp, if, else, for ***
# s=[x if x%2==0 else 0 for x in range(10)]
# s1=[x for x in range(1,11) if x%2==0]
# print(s1)

# ====================================================================================================================
# Tuple datat type**
# read only version of list
# immutable (non changeable behaviour)
# 21,"saransh"


# 1> tuple is exactly same as list except tuple is immutable
# 2> once we creat the tupe object, we cannot perform any changes.
# 3> hetrogenious is allowed (i.e 1,'saransh')
# 4> duplicate allowed
# 5> Insertion preserved
# 6> indexing and slicing
# 7> tuple creat wint '()' with ','

# s=()
# print(type(s))

# s1=(10)   ===> Not tuple

# s2=(10,) ===> tuple

# s3=10,20,30  ===> tuple

# Sorted
# s=(4,5,8,9,1,0)
# s1=sorted(s)
# print(s1) #assending order
#
# s2=sorted(s,reverse=True)
# print(s2) #desending order


# m=(1,2,3,[2,3,4],89,"saransh")
# # in all data tuple () is used
# # in tuple there is a index[] and string""
# m1=m[3]
# m1=append("saransh")
# print(m1)
# print(m)

# Min and Max
# by default it will sort
# find out min and max value from tuple

# s=(10,20,30,40)
# print(min(s))
# print(max(s))

# Packing Unpacking

# unpacking to packing
# a=10
# b=20
# c=30
# s=a,b,c  #packing
# print(s)

# packing to unpacking
# s=(10,20,30)
# a,b,c=s
# print(a)
# print(b)
# print(c)

#---------------------------------------------------------------------------------------------------------------------
# SET {}*

# Pop & Remove
# it remove random element ----> pop()

# s={'saransh',1,2,3,4,5}
# print(s.pop())
# print(s)

# remove---> specific element remove

# s={1,2,3,4}
# s.remove(4)
# print(s)
# key error if value is not present

# Discard
# s={1,2,3,4}
# s.discard(3)
# print(s)

# Clear
# to remove all element

# s={1,2,3,4,5}
# s.clear()
# print(s)

# Union() ; intersection() ; difference() ; symetrical difference()
#  The above code are mathematical

# ^, |, -, &

# Union (|) " | (pipe operator)" ====> to return all element
# s={1,2,3,4}
# s1={3,4,5,6}
# print (s | s1) #o/p--{1,2,3,4,5,6}
# # or
# print(s.union(s1)) #o/p--{1,2,3,4,5,6}

# Intersection (&)
# it will return common element
# s={1,2,3,4}
# s1={3,4,5,6}
# print(s&s1) #o/p--{3,4}
# # or
# print(s.intersection(s1))#o/p--{3,4}

# Difference (-)
# s={1,2,3,4}
# s1={3,4,5,6}
# print(s-s1)#--{1,2}
# # or
# print(s.difference(s1))
# # s-s1---> element present in s but not in s1
# s={1,2,3,4}
# s1={3,4,5,6}
# print(s1-s)#--{5,6}
# # or
# print(s1.difference(s))
# s1-s---> element present in s1 but not in s

# symetrical difference(^)
# common element will not print
# element present in either x or y
# x={1,2,3,4}
# y={3,4,5,6}
# print(x^y)#o/p--{1,2,5,6}

# Set comprehension
# s={i*i for i in range(5)}
# print(s)

# --------------------------------------------------------------------------------------------------------------------
# Dictonary***

# d=dict()
# d1={}

# key value pair data
# s={key:value}
# s={"math":"value"}
# s1={"math":98,"english":88,"hindi":78}
# #Duplicate keys are not allowed, if you take it so it will over write the value of latest one.
# s1={"math":98,"math":88,"hindi":78}
#
# d={[123]:"saransh"}   #Not allowed
# d1={(123,):"saransh"} #Allowed

#Insertion order is not support
#Indexing slicing not allowing
#No duplicate key

# s={}
# # # s1={'mm':5,'sw':0.5,'nc':5,'ml':0}
# #
# # # name, age, no.
# # # How to put values in Empty dictonare?
# s['name']='saransh'
# s['age']= 24
# s['no']=9096640388
# print(s)

#Update the above values?
#update the no. (i.e replace it)
# s={}
# s['name']='saransh'
# s['age']= 24
# s['no']=9096640388
# print(s)
#
# s['no']=1234567890
# print(s)

#How to get specific info. from dict?
# s1={'mm':5,'sw':0.5,'nc':5,'ml':0}
# print(s1['nc'])

#if we want to delete the key
# del(s1['ml'])
# print(s1)

#--------------------------------------------------------------------------------------------------------------------
# len ----> to check the length
# clear ----> it will remove the value from distonary.

# Get function
# if Ke is not present in the Dict. then it show None when using get()
# s={'a':1, 'b':3,'c':4}
# print(s['b'])
# print(s['z']) #o/p---Key error
#
# print(s.get('b'))
# print(sget('z')) #o/p---None
#
# s['d']=5
# print(s)

#Pop()
# specific key will remove
# s={'a':1, 'b':3,'c':4}
# print(s.pop('a')) #o/p---1
# print(s)

#Popitem()
# last key&value will remove
# s={'a':1, 'b':3,'c':4}
# print(s.popitem()) #o/p---c,4
# print(s)

# Keys()***
# How to find out only keys?
# s={"math":98,"english":88,"hindi":78}
# print(s.keys())
# for i in s.keys():
#     print(i)

#values()
# s={"math":98,"english":88,"hindi":78}
# print(s.values())
# for i in s.values():
#     print(i)

# Items()
# to show thw both(key : value) from dict
# s={"math":98,"english":88,"hindi":78}
# for k,v in s.items():
#     print(k,v)

#Copy()
# s={"math":98,"english":88,"hindi":78}
# s1=s.copy()
# s1['math']=20
# print(s1)

# Set Default()
# if we want to change a specific key & value
# s={"math":98,"english":88,"hindi":78}
# print(s.setdefault('math',50))
# print(s.setdefault('python',79))
# print(s)

#Update
# To update, it will print at last
# s={"math":98,"english":88,"hindi":78}
# s.update({'java':88,'python':89})
# print(s)

# DictComprehension
# s={x:x*x for x in range(1,11)}
# print(s)

# ----------------------------------------------------------------------------------------------------------------------

# print(10+20)
# a=10
# b=20
# print(a+b)
# s=int(input('enter your first value'))

# FBV:- Function base view
# CBV:- Class base view

# Function:- using def keyword
# if a group of statement is repeatedly required so we will write in function and  will call that function
# value inside () is called parameter.
# there are 4 type of parameter

# multiple two digit addition?

# if there is repated code we write in function code, & we call it multiple time.

# code redundancy :- kamit kami line

# different between print and return?

# def add(x,y):   #print
#     print(x+y)  #return
# add(10,20)
# add(1,2)
# add(48,57)
# doc string :- """  """. Under def. what o/p we want/show

# Two types of function?
# 1.build in function :- it is given by python [type(), id(),pop(), update()]
# 2.user define function :- a function define by user

# def wish(name):
#     print("hey",name,'good morning')
# wish('mrunmayee')
# wish('saransh')

# Q.> difference between sort and sorted?
# ==> in sorted we have to take new variable. assending order o/p in list

# Q.>different between print and return?
# when we write return 'inside' function, then it will become its print value, one function on return. you can directly
# call the function.
# Print can use 'inside' as well as 'outside' of function.
# example:-
# def wish():
#     print('hello')
# wish()
# wish()
#
# def wish1():
#     return 'hello all'
# a=wish1()
# print(a)
#
# b=wish1()
# print(b,'developer')

# def wish(name):
#     return name
# a=wish('saransh')
# print(a)

# def wish():
#     print('hello')
# print(wish())
# print(wish(),'saransh') #o/p none saransh
#
# def wish1():
#     return 'hello all'
# s=wish1()
# print(s,'saransh') #o/p hello all saransh

# If a group of statement repeatedly required then it is not recommended to write, this statement every time seprately.
# We have to define this statement as a single unit and we can call  that unit any no. of time based on our requirement,
# without re-write. This unit is nothing but the 'FUNCTION'.
# The main adv. of function is code reusable. Python define 2 type of statement
# 1>Built-in function :-function comes along with [type(), id(),pop(), update()]
# 2>User define function :-the function define by the user
#
# Using function Print odd & even
# use print not return
# eg- if even print(even), odd print(odd)?

# def odd_even(no):
#     if no % 2 == 0:
#         print('even')
#     else:
#         print('odd')
#
# odd_even(18)
# odd_even(7)

# PARAMETER / Argument :-They are input to the function, if a function contain parameter & at the time of calling
# it is compulsory we should provide value, otherwise it get error. It will inside '()'

# def wish(name):
#     print (name)
# wish ('saransh')

# Types of Arguments*
# a.formal - def wish(name,age):
# b.actual - def wish ('saransh', 25):

# 1.> Positional Argument
# these are the argumnet pass to the function in correct position order.parameter wise
# When we pass formal argument(fa) & actual argument(aa) the value will decided by it's sequence.

# aa = (a,b,c)
# aa = (1,2,3)

# def add(c,b,a):
#     print(a)
#     print(c)
#     print(b)
# add(5,2,7)
#
# def operation(a,b):
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a/b)
# operation(1,2)

# 2.> Keyword Argument
# parameters's key value pass krna hai ; sequence is not imp., count is imp. while calling the function
# when to give keyword arg.?

# def keywordss(name,age):
#     print("my name is",name,"and my age is",age)
# keywordss(name='saransh',age=25)
# keywordss(age=25,name='mrunmayee')
# # keywordss(age=24) #type error

# positional + keyword => 1st when we call function, take positional argument, 2nd agrument take keyword
# def wish(name,age):
#     print("my name is", name, "and my age is", age)
# wish('saransh',25)
# wish('kuki', age=25)
# wish(name='mrunmayee', 29) #syntex error


# 3.> Default Argument
# we pass the by default parameter
# def wish(name='saransh',age=25):
#     print("my name is", name, "and my age is", age)
# wish() #o/p-my name is saransh and my age is 25
# wish("kuki",22) #o/p-my name is kuki and my name is 22
# wish('mrun', 24)

# 4.> Variable length Argument***
# Q.> What is the diff. between * args and **keywordargs?

# A.> *args:- *-we can pass any no. of parameters at the time of calling.

# def wish(*args): #eg:- (name,age,cit,no.)
#     for i in args: #for loop
#         print(i)
# wish(2,3,4)
# wish(1,2,3,4,5,6)

# B.> **kwargs:- we can pass any no. of keys & value at the time of calling.
#
# def wish(**kwargs):
#     for k,v in kwargs.items(): #for loop
#         print(k,v)
# wish(name='saransh',age=25,city='nagpur')
# wish(city='Mumbai',age=22)



# inside the function:-
# def wish():
#     print(90) #inside
# wish()
# outside the function:-
# a=20 #outside
# def wish():
#     print(90) #inside
# wish()
#---------------------------------------------------------------------------------------------------------------------

# Type of variable
#
# 1.> Global variable
# 2.> Local variable

#---------------------------------------------------------------------------------------------------------------------

# In interview we have to basic function.(basic coding)

# Lambda***
# it is a nameless function
# it is a Anonoymous function :
#Q.> what is means by lambda
# -> sometime we can declear the function without any name, such type of function are called anonoymous function.

# use for instant use
# for one time use (i.e. cannot call multiple time), because it is a nameless function.
# lambda function internally return expresion value and we are not req. return statement expesitvely.
# we can use lambda function with filter(), map() and reduce()

# def lam #incorrect
# lambda #correct
# use directly
# EXAMPLE
# def sqr(n):
#      print(n*n)
# sqr(5)


# syntax of lambda
# s =lambda n : n*n
# print(s(4))

# s =lambda n,m : n*m
# print(s(4,9))

#  lambda n,m,l,g:n+m+l+g

# def add(a,b):
#     print(a+b)
# add(10,20)
#
# a= lambda n,m : n+m
# print(a(10,20))
#
# s=[1,4,2,5,3]
# sort the list using Lambda?

# Using ternary
#
# exp1 if condition else exp2
#
# a,b = 10,20
# d= a if a> b else b
# print(d)
#
# s= lambda a,b:a if a> b else b
# print(s(10,20))
#
# Q.> difference between simple/regular function and lambda function?

# FILTER Function :
# eg
# s=[1,2,3,4,5,6,7,8]
# s1=[]
# for i in s:
#     if i%2==0:
#         s1.append(i)
# print(s1)  #2468

# filter(): it will filter the value, based on some condition
# expression/syntex :- filter(function,sequence) # function=expectively/expectedly i.e we have to write condition

# d=[1,2,3,4,5,6,7,8]
# def even(x):
#     if x%2==0:
#         return True
#     else:
#         return False
#
# s=filter(even,d) #o/p will be in object
# #s=list(filter(even,d)) # we use list/tuple/set/string here because the above o/p is coming in object.
# print(s)
#
# s1=[1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19]
# s2=list(filter(even,s1))
# print(s2)
#
# s3=list(filter(odd,s1))
# print(s3)

#filter using lambda ()
# d=[1,2,3,4,5,6,7,8]
# s =filter(lambda x : x%2==0,d)
# print(list(s))

# Map ()
# it is used to apply functionality in the seq.
# every element present in the give seq. apply some functionality,
# and generate mew element with req. modification/functionality

# Syntax of Map()
# map(function,seq.)

# d=[1,2,3,4,5]
# def double(x):
#     return x *2
# s=map(double,d) #o/p will be in object
# s=list(map(double,d))
# print(s)

# Reduce()
# it will reduce the seq. of the element into a single element by appling some function.
# we cannot use directly, it is writen in pythons funtools(induild)
# reduce syntax
# reduce(function,seq)

# EXample
# s=[1,2,3,4,5] #addition of the value i.e 15
# from functools import reduce
#
# numbers = [1, 2, 3, 4, 5]
# result = reduce(lambda x, y: x + y, numbers)
# print(result)  # Output: 15


# a=10
# b=20
# c=30
# def reduce():
# #
# # from funtools import * #* means all
#
# g=[1,2,3,4,5,6]
# s=reduce(lambda x,y: x+y,g)
# print(s)

# c=[1,2,3,4,5,6]
# def add(x,y):
#     return x+y
# s = reduce(add,c)
# print(s)

# function ALISING

# def wish():
#     print('hello')
# saransh=wish
# saransh()
# wish()

# def wish(): #outher function
#     print('thos os a wish function')
#     def wish1(): #inner function i.e nested
#         print('thiis is a nested function')
#     wish1()
# wish()


# DECORATOR*** :-
# it is a function which can take a function as a argument/parameter and extend functionality
# and return modified function.

# EXAMPLE

# def wish(name) :
#     # print('hello',name)
#     if name=='mrunmayee':
#         print('ssd')
#     elif name == 'saransh':
#         print('pm')
#     else:
#         print('hello',name)
# wish('saransh')
# wish('mrunmayee')

# FOLLOWING IS THE CORRECT EXAMPLE

# def decor(wish1): #here we will modify the function
#     def inner(name):
#         if name =='mrunmayee':
#             print('ssd')
#         elif name == 'saransh':
#             print('pm')
#         else:
#             wish1(name)
#     return inner
# @decor  #outter function name

# def wish1(name): #this is the main function, we are not modifying it
#     print('hello',name)
# wish1('mrunmayee')

# write one decor(), here we need to divide two parameter, if value of denominator is zero then msg populate like
# ("we can't divide be zero")



# def decor(func):
#     def inner():
#         print('before main function') #step 1
#         func()
#         print('after main function') #step 3
#     return inner
#
# @decor
# def main():
#     print('main function') #step2
# main()

# GENeRATOR
# it is a function which is responsiblity to genrate seq. of the value.
# instead of return we use yeild keyword to return the value
# to shoe\w the seq. of value using next()


# Advantage
# it improv-e memory utilization and performance
# it is sutiable example to read data from large file.

# CONCEPT 1
# def wish():
#     yield 'abcd'  #we can use multipal time yeild
#     yield '1234'
# s= wish()
# print (type(s))
# print(next(s))
# print(next(s))

# CONCEPT 2
# def wish():
#     yield "a"
#     yield "b"
# s=wish()
# print(s) #o/p object
# for i in s:
#     print(i)


# Q.> difference between list comprehension and genrator?


# Q.> fibbonaci series :#0,1,1,2,3,5,8,13
# Q.>using generator countdown & countup :
# def countdown(num):
#     while num > 0:
#         yield num
#         num = num-1
# d=countdown(5)
# # print(next(d))
# # print(next(d))
# # print(next(d))
# # print(next(d))
# # print(next(d))
#
# for i in d:
#     print(i)

#RECURSIVE function
# function under the function

# def wish():
#     return 1
#     wish()

# factorial :-5*4*3*2*1

# MODULE AND PACKAGEs:
# import, from

# what is meant by moduel?
# it is nothing but the python file. #xyz.py
# a group of  variable name, function name , class name  saved to the file is nothing but module

# for variable
# x=10
# y=20

# with help of import
# import classes #at another .py file
# print(abcd.x)

# with the help of from
# from classes import x,y  #at another .py file
# print(x)

#Q.> Difference between import and from ?

# def wish(name):
#     return f"{name},good morning"
# s=wish("saransh")
# print(s)
#
#
# import abcd #at another .py file
# print(abcd.wish("mrunmayee"))
#
# d=abcd.wish("virat")
# print(d)
#
# from abcd import wish #at another .py file
# print(wish('rohit'))

# PACKAGE
# a group of moduel is nothing but package

# dir ()?

# As()
# import classes as a #we can use any name as
# print (a.s)

#---------------------------------------------------------------------------------------------------------------------
# ADVANCE PYTHON

# OOPS*
# inheratance, abstract, encapsulation, Polymorphism
# I P A E :-

# class, variable, method, obh=ject, self constructor,type of Inheritance, I P A E, MRO, setter getter method

# What is meant by class?
# -> in python everything is object, to create a object we req. some model(table) or
# blueprint or plan which is nothing but the class.
# we use class ke function

# a=10
# b=20
#
# class Saransh :#It should start with Capital letter
# # inside class there is variable and method and constructor
#
#
# def wish():
#     print("morning")   #this is a Function, as it is outside of class
#
# class Saransh:
#     a=10
#     def wish(self): #this is a Method
#         print(self.a)

# Q.> different between function and method?
# function is outside of class and method is inside of the class

# Type of method(action) :- instance, static, class method
# Type of variable(properties) :- Instance, static, local variable

# Q.> what is meant by object?
# as we call the function, just like that to call the class we need object

# def wish(name):
#
# class S:
#     def __init__(self):

# Q.>what is constructor?
# it make inside the class, it name is "__init__".It is also called dunder method (start and end with "__  __").
# By default Parameter is (self), but we can change it. In a class we use in "__init__" and multiple methods
# it will print dock string. It will use to make instance variable.

# Pillers of OOPS

# Inheritance:- The property of parent class, that can be use by child class is called inheritance
# single, multiple, multilevel, hierarchical, hybride

# Polymorphism
# any operator which has multiple uses i.e "+ , *"

# encapsulation
# use to data hide

# abstraction
# use to data hide

# class A: #first letter is always capital
    # """ docstring""" #not mandatory

# class B:
#     """this is a simple class"""
# print(B.__doc__)


# class C: #this is your class
#     def __init__(self): #this is your constructor
#         self.a=10  #this is your instance variable
#         self.b=20
#
# # Note :- Constructor makes only once, but we create Multiple instance variable.
#
#     def im(self): #this is your method
#         print(self.a + self.b) #this is your instance method
# # Note :- Constructor makes only once, but we create Multiple method and instance method.
#
#     def wish(self):
#         print("this is a wish method")
# s=C() # here "s" is refrance variable and complete make it object. Constructor not need to call seprately
# # Now we have to call Instance method
# s.im()
# s.wish()

# Q.> what is mean by object? and what is refrance variable?
# physical existance of the class is object. it is made my refrance variable

# Q.> differance between constrator and method?
# constructor is a special method in python
# the name of constructor should be __init__(self)
# no need to call sepeately, while creating the object it will automatically call
# constrator can take atleast one parameter (self)
# the main purpose to initialize instance variable


# Q.> What is instance method/variable?


# CONSTRUCTOR / SELF VARIABLE :

# physical existance of the class is called odject.

# Q.> what is self variable?
# self is a default variable, which is always pointing to the current object
# by using self we can access instance variable and instance method of the object


# class Student:
#     def __init__(self,name,age):
#         self.name = name #we can write self.a OR self.x OR self.name
#         self.age = age
#
#     def display(self):
#          print(f'my name is{self.name} and my age is {self.age}')
#
# c=Student('saransh',25) # this is your object
# c.display()
#
# c1=Student("mrunmayee",24)
# c1.display()

# TYPE of Variable

# 1.)Instance variable:
# if the value oof variable is varied from object to object such type of variable is called instance variable.
# instance methode is made inside constructor
# EXAMPLE
# class Student:
#     def __init__(self):
#         self.a=20
#         self.b=30
# s=Student()
# print(s.__dict__)

# A) inside the INSTANCE METHOD

# class Maths:
#     def __init__(self):
#         self.a=10
#
#     def xyz(self):
#         self.b=20
#
# s=Maths()
# s.xyz()
# print(s.__dict__)

# B) outside of the class : using ref. variable
# class Exercise:
#     def __init__(self):
#         self.a=31
#     def wish(self):
#         self.b=32
# s=Exercise
# s.wish()
# s.d=40 #this is your ref. variable which is outside of the class
# print(s.__dict__)


#2.)static variable:
# if the value oof variable is not varied from object to object such type of variable is called static variable.
# object to object change nahe hoot.
# A)
# class A:
#      x=10 #this is your static variable , which is outside the function & inside class
#      def __init__(self):
#          self.a=20
#      def wish(self):
#          self.c=30



#3.)local variable:

# Q.>diff betwn instance and static variable?



# CLASS METHOD
# Static variable --- can't be changed  from object to object,
# can be called without making an object, used inside the class outside the method.

# class A:
#       x = 10
#       y = 21
#       @classmethod
#       def wish(cls):
#          print(cls.x * cls.y)
# A.wish()

# class Animal:
#       legs = 4
#       name= "dog"
#       @classmethod
#       def walk(cls,name):
#           print(cls.legs)
#           print(cls.name)
#           print(f'{name} walks with {cls.legs} legs.')
# Animal.walk("dog")

# Static method: General utility method, decorator is used in static method. Can't use instance variable or static variable

# class A:
#      @staticmethod
#      def wish(x,y):
#          print(x+y)
# A.wish(10,20)

# Class method is rarely use.

#  Q.> can you used class method in static variable?
# -> yes

# Q.> diff betwn instance method and class method?


# places where static variable can make?

# 1> ingernal we can creat stacic variable inside the class, but outside the method
# class A:
#     x=10
#     def wish(self):

# 2.> Inside the constrator, using the class name
# class A:
#     x=10
#     def __init__(self):
#         A.y=20 #using class name
#         # self.c=30 #instant variable
#     def wish(self):

# 3.> inside a instance method using class name
# class A:
#     x = 10
#     def __init__(self):
#         A.y = 20  # using class name
#     def wish(self):
#         a.z=40

# 4.> inside the class method using class name or cls parameter
# class A:
#     x = 10
#     def __init__(self):
#         A.y = 20  # using class name
#     def wish(self):
#         a.z=40
#     @classmethod
#     def wish2(cls):
#         A.q=60 #using class name
#         cls.s=70 # using cls parameter

# 5.> inside static method using class name
# class A:
#     x = 10
#     def __init__(self):
#         A.y = 20  # using class name
#         print(A.y)
#
#     def wish(self):
#         a.z=40
#
#     @classmethod
#     def wish2(cls):
#         A.q=60 #using class name
#         cls.s=70 # using cls parameter
#
#     @staticmethod
#     def wish3():
#         A.l=80

# MRO -

# nheritanceI:- The property of parent class, that can be use by child class is called inheritance

# TYPE of Inheritance

# single :-
# multiple
# multilevel
# hierarchical
# hybrid


# property -> variable
# action -> method

# a.> code reusability
# b.> Real time relationship

#1.> single Inheritance:-
# when child class inherit only one parent class is called single Inheritance.

# class A:
#     def  first(self):
#         print("this is a first method")
#
# class B(A): #here A is parent class and B is a child class.
#     def second(self):
#         print("this is a child class property")
# obj=B()
# obj.second()
# obj.first()

# 2.> multiple Inheritance:-
# when a child calss inhert from more than one parent class.
# class A:
#     def parent1(self):
#         print("this is parent 1 property")
#
# class B:
#     def parent2(self):
#         print("this is parent 2 property")
#
# class C(A,B):
#     def child(self):
#         print("this is child class")
# obj=C()
# obj.parent1()
# obj.parent2()
# obj.child()

# 3.> Multilevel Inheritance:-
# when child class become a parent class for another child class

# class A:
#     def a1(self):
#         print("this is A property")
#
# class B(A):
#     def b1(self):
#         print("this is B property")
#
# class C(B):
#     def c1(self):
#         print("this is C property")
#
# obj=C()
# obj.a1()
# obj.b1()
# obj.c1()

# SUPER METHOD/FUNCTION :- this allows us to call a method from parent class
# this writes under class

# class A:
#     def  first(self):
#         print("this is a first method")
#
# class B(A): #here A is parent class and B is a child class.
#     def second(self):
#         print("this is a child class property")
#         super().first()
# obj=B()
# obj.second()

# 4.>hierarchical Inheritance:-
# inherit from same parant classs

# class P:
#     def common(self):
#         print("tnis is a parent class property")
#
# class C1(P):
#     def c1(self):
#         print("this is a c1 class property")
#
# class C2(P):
#     def c2(self):
#         print("this is a c2 class property")
#
# obj1=C1()
# obj2=C2()
#
# obj1.common()
# obj1.c1()
#
# obj2.common()
# obj2.c2()

# Polymorphism :- manyform (+ , *)
# poly-> many
# morph-> forms

# overloading --> We can use same operator(+,*) or same method for different purpose.
# a.> operator overloading (+,*)
# + --> 1. addition 2. concatation
# * --> 1.multiplaction 2.repeatation

# b.> method overloading #do not support in python
# c.> constroctor overloading  #do not support in python

# overriding --> Whatever member are available at parent class, by default available to child class through the Inheritance
#  and if,child class not satisfied to parent class implementation, then child class is allowed to redefine the method in
# the child class , this concept is called overrinding

# a.> method overriding:-

# class P:
#     def c1(self):
#         print("sdfg")
# class C(P):
#     def  c1(self):
#         print("sdfgn")
#         super().c1()
#
# obj=C()
# obj.c1()



# class P:
#     def property(self):
#         print("gold","house","car")
#
#     def marry(self):
#         print("deepika")
#
# class C(P):
#     def marry(self):
#         print("alia")
#         super().marry()
#
# obj=C()
# obj.marry()
# obj.property()



# b.> constructor coveriding :-

# class P:
#     def __init__(self):
#         print("saransh")
#
# class C(P):
#     def __init__(self):
#         print("Mrunmayee")
#         super(). __init__()
# c=C()



# Abstraction :- depends on ABC

# Encapsulation :- depends on private method and private variable ;
# we cannot call directly(restriction:- you can restrict to private and direct variable ), call using self.

# both use to data hide

# class A:
#     def wish(self):
#         print("abcd")
# s=A()
# s.wish()

# Private Method
# class A:
#     def __wish(self):   #strongly private
#         print("abcd")
#
#     #to call the strongly method function
#     def a1(self):
#         self.__wish()
# # s=A()
# # s.__wish() #we cannot call directly , so this is wrong coding
#
# B=A()
# B.a1() # this is correct coding

#Private variable
# class A:
#     a=10 # this is static variable
#     __a=10 #private variable
#     def display(self):
#         print(self.__a)  #using self, we have to call
#
# C=A()
# C.display()

# Abstraction
# Q.> abstract method and class ?
# Abstraction classes are classes that contain one or more abstract method.
# Abstract method -> it is method that declared, but contain no implementation. @abstractmethod


# from abc import ABC, abstractmethod # this is your parent class of your abstract
#
# class A(ABC): #this is a child class of ABC
#     @abstractmethod
#     def wish(self):
#         print("saransh")
#     # you cannot call directly
#
#     @abstractmethod
#     def wish1(self):
#         print("saransh")
#     #we have to implement all abstract method.
#
# class B(A):
#     def wish(self):
#         print("virat")
#
#     def wish1(self):
#         print("kohli")
#
# o=B()
# o.wish()
# o.wish1()


# Regular expression (RE)(regex)
# if we want to represent a group of string according to particular formate/pattern, then you should regular expression.
#string data type

# 1.>compile()  #its a functionality in RE
# any pattern in the string i.e repeatation of word (eg-abcabcabcabc),so to convert into regex by compile
# re module contain compile() function  to compile a pattern into regex object



# import re
# re.compile()
# s1="abc111abc111abc123abc111abc112"
#
# s=re.compile('111')

# 2.> finditer()
# a.> start
# b.> end
# c.> group

# s.finditer(s1)

# import re

# s1="abc1234abc345abc678"
# s=re.compile("abc")
# d=s.finditer(s1)
# for i in d:
#     print(i.start(),i.end(),i.group())
# o/p :-
# 0 3 abc
# 7 10 abc
# 13 16 abc


# without using compile
# a=re.finditer("abc","abc1234abc345abc678")
# for i in a:
#     print(i.start(),i.end(),i.group())


# CHARACTER CLASSES:-
# it denotes in []
# eg:- [abc] a b c
# cap symbole ^ , it will not print what we have write in sq.bracket
# eg:- [^abc]
# s="abcabcb@#$#$#1555666 cabcAAAAAZZZZZZBBBBB"

# import re
#
# a=re.finditer("[abc]","abc1234abc345abc678")
# for i in a:
#     print(i.start(),i.end(),i.group())


# import re
#
# a=re.finditer("[^abc]","abc1234abc345abc678")
# for i in a:
#     print(i.start(),i.end(),i.group())


# import re
#
# a=re.finditer("[a-z]","abc1234abc345abc678msn@#$ABC")
# for i in a:
#     print(i.start(),i.end(),i.group())



print("hello word")
# import re
#
# a=re.finditer("[a-zA-Z]","abc1234abc345abc678msn@#$ABC")
# for i in a:
#     print(i.start(),i.end(),i.group())

# PRE DEFINE CHARACTER CLASSES
# we do not need to write in []
#
# \s --> space #it will find space
# \S --> expect spce  #it will print expect space
#
# \d --> digit
# \D --> expect digit
#
# \w --> word character  # it will find [a-z A-Z 0-9]
# \W --> special character
#
# . --> all character


# QUNTIFIRES:

# s= "abaabaaab"

# a --> exactly one a
# a+ --> atleast one a
# a* --> any no. of a, including zero no.
# a? --> atmost one a , including zero no.
# a{2} --> exactyt no. of a
# a{2,3} --> {min. no. of a , max. no of a}

import re
# m=re.finditer("a", "abaabaaab")
# for i in m :
#     print(i.start(),i.group())

# m=re.finditer("a+", "abaabaaab")
# for i in m :
#     print(i.start(),i.group())

# m=re.finditer("a*", "abaabaaab")
# for i in m :
#     print(i.start(),i.group())

# m=re.finditer("a?", "abaabaaab")
# for i in m :
#     print(i.start(),i.group())

# m=re.finditer("a{2}", "abaabaaab")
# for i in m :
#     print(i.start(),i.group())

# m=re.finditer("a{2,5}", "abaabaaaaaaaaaaaaaaaaaaaaab")
# for i in m :
#     print(i.start(),i.group())


# important function of re module

# "i am in mumbai"

# 1.> match() --> it wii check beginning of the string
# iam  IAM , it will show false o/p as it is a case sensitive
# import re
# s=re.match("i am", "i am in mumbai")
# print(s)
#
# import re
# s=re.match("i am", "i am in mumbai")
# if s!=None:
#     print("yes this string start with i am")

# 2.> fullmatch() --> it check the complete string
# import re
# s=re.fullmatch("i am", "i am in mumbai")
# print(s)
#
# import re
# s=re.fullmatch("i am in mumbai", "i am in mumbai")
# if s!=None:
#     print("yes this string start with fullmatch")
# else:
#     print("no match")


# 3.> findall()
# 4.> fintiter()
# 5.> sub()
# 6.> subn()
# 7.> split()
# 8> compile()


# from practice import maths
# x = 111
# maths(x)