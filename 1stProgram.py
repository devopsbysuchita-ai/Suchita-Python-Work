#Print the Word
print("Helo World,")
print ("Good Morning")

#Decalre the variables
name = "Suchita Sargar"
age = 30
old = False
Price = 25.99
x = None

#Print the Word by using Variable
print("My Name is: ", name)
print("My Age is: ", age)

#Types of Datatypes in Python
#integers
#string
#float
#boolean
#none

#print the Datatype of variable
print(type (name))
print(type(age))
print(type(Price))
print(type(old))
print(type(x))

#Keyword: Kewords are reserved words in python

# Comments in Python
# Single Line: #
# Multiline: """   """

#Tyeps of operators

""" 
An Operator is an symbol that certain operation between operands
Arithmatic (+, *, %, /, **)
Relational/Compariason (==, !=, >, <, >=, <=)
Assignment (=, +=, -=, *=, /=, %=, **=)
Logical (not, and, or)
"""
#Arithmatic operator
a = 1500
b=20
print("Addition is: ", a+b)
print("Multiply is: ", a*b)
print("Divide by is: ", a/b)
print("Reminder is: ", a%b)
#Another way to get result
Sum=a+b
Multi=a*b
Divide=a/b
Modulo=a%b #return reminder
print(Sum)
print(Multi)
print(Divide)
print(Modulo)

#Relational Operators
abc=50
xyz=100
print("Is abc equal to xyz:", abc==xyz) #False
print("Is abc not equal to xyz:", abc!=xyz) #True
print("Is abc greater Than to xyz:", abc>xyz) #False
print("Is abc less than to xyz:", abc<xyz) #True
print("Is abc greater that equal to xyz:", abc>=xyz) #False
print("is abc less that equal to xyz:", abc<=xyz) #True

#Assignment Operators 
num =10
print("= Ans is :", num)
num1 =20
num1 += num1
print("+= Ans is :", num1)
num2 = 30
num2 -= num2
print("-= Ans is :", num2)
num3= 30
num3 *= num3
print("*= Ans is :", num3)
num4 = 50
num4 /= num4
print("/= Ans is :", num4)
num5=60
num5 %= num5
print ("%= Ans is :", num5)
num6=60
num6 **= num
print ("%= Ans is :", num6)

#Logical operator : for Boolean Value
X=10
Y=40
print (not False)
print (not (X < Y))

val1 = True
val2 = True
print("and operator is :", val1 and val2)
val3 =True
Val4 =False
print("and operator is :", val1 and val2)
# if both value same then we will get ans Ture otherwise we will get False

print("or operator is :", (X == Y) or (X < Y))
print("or operator is :", (X == Y) or (X > Y))
#if any expression returns True we will get true otherwise will get False


#Type Conversion
#Convert the type from one to another type which is called as Type Conversion
#two types of Type conversion we have in python 
#1) Type Conversion : It's automatic Conversion
# 2) Type Casting : It's manual Conversion. needs to inform the program that we want convert the type

W=10
Z=20.2
T=W+Z
print("Sum IS: ", T)
#here W is int and Z is Float. when we are using arithmatic opertor to calculate we will automatically get ans in Float type because flot is superior type as compare to int. it's implicit conversion.

A= int("4")
B= 20.4
print(type(A))
print(A+B)
#here We are manually converting type string to int. this is explicit conversion.


#Input in Python

Name=input("Enter Your Name: ")
print("Hello,", Name)
print(type(Name))
#get the type of input value
Age=int(input("Enter your age: ")) #Converting the type into int
print("Your Age is: ", Age)
print(type(Age))

"""output will be <class 'str'> becaue input always return string type. 
so if we want to return in actual type then we need to covert the type"""

#Practice Question
#Write a Program to input 2 numbers and print their sum

Num1=int(input("Enter First Number: "))
Num2=int(input("Enter Second Number: "))
print("Sum Is: ", Num1+Num2)

#Write a Program to input side of square and print it's area

Side=int(input("Square Side is: "))
print("Area is: ", Side*Side)

#Write a Program to input two float numbers and print their avarage

N1=float(input("Enter First Num: "))
N2=float(input("Enter Second Num: "))
print("Average is: ", (N1+N2)/2)

#Write a program to input two numbers,a and b and print true if a is greater than equal to b if not print false

a1=int(input("Enter a First Number: "))
b1=int(input("Enter a Second Number: "))
print(a1>=b1)











