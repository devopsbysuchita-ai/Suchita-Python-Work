#String and Conditional Statements

#String
#String is a data type that stores a sequence of character

#Escape sequence Charaters: 
# it's special charaters which used for formating like tab and sentences in new line etc.

str="This is a String. which we writing in python."
print(str)
#by using escape sequence charater \n
str1="This is a String. \nwhich we writing in python."
print(str1)
#by using escape sequence charater \t
str2="This is a String. \twhich we writing in python."
print(str2)

#Basic Operation 
#1) Concatenation: operation adding two string it's called as concatenation. 
# we are using + sign to perform concatenation
#"Hello" + "World" = "HelloWorld"

a="Suchita"
b="Jankar"
print(a+b)
print(a+ " " +b) #added space between two string

#2) length of Str: we are using len function to calculate the length of string. spaces also will be calculated in string
#len(Str)

Name="Omkar Jankar"
print(len(Name))

#Indexing
#it means each charaters gets it's own position number.
#for eg  S U C H I T A
#        0 1 2 3 4 5 6
#by using index we can print exact index charater
name="Suchita"
print(name[3])


#Slicing: Accessing parts of string. meaning breaking string in two parts
#Str[staring_idx:ending_idx] //ending index is not included

Str="Suchita Sargar"
print(Str[3:6]) # it's returning charters from index 3 to 5 o/p=hit
print(Str[8:]) # [8:len(Str)] o/p Sargar

#Slicing Nagative index : it willl count from backwords and indexing will start from -1

#eg: A  P  P  L  E
#   -5 -4 -3 -2 -1

Str1="Omkar"
print(Str1[-3:-1]) #o/p ka it's doesn't include ending index

#String Function

Str3="i am a Coder"

#Str3.endswith("er") //returns true if string ends with er

print(Str3.endswith("er"))

#Str3.capitalize() //Capitalize 1st char

print(Str3.capitalize())

#Str3.replace(old,new) //replaces all occurences of old with new

print(Str3.replace("Coder", "Engineer"))

#Str3.find(word) //returns first index of 1st occurence

print(Str3.find("a")) #here first we have in am so it's returning index 2

#Str3.count() // returns counts the occurance of substring

print(Str3.count("a"))

#Practice questions

#Write a program to input user's name and print it's length

Name=input("Enter Name: ")
print(len(Name))

#Write a program to find the occurance of $ in a string

Val="How$ What$"

print(Val.count("$"))


#Conditional Statements
#if-elif-elas

#Syntax
"""
if(Condintion):
Statement1
elif(Condition):
Statement2
else:
StatementN

"""

Age=12

if(Age>=18):
    print("Eligible")
else:
    print("Not Eligible")


Marks=74

if(Marks<=40):
    print("Grade C")
elif(Marks<=50):
    print("Grade B")
else:
    print("Grade A")

#Nesting : onse statement inside an another statement

age= 12
if(age>=18):
    if(age>=80):
        print("Cannot Drive")
    else:
        print("Can Drive")

else:
    print("Can not Drive")


# Practice Question

#WAP to check if a number is even or odd

val1=9
if(val1%2==0):
    print("Even")
else:
    print("odd")

#WAp to find greatest number of three numbers

a=4
b=1
c=8

if(a>b and a>c):
    print("a is greater")
elif(b>c):
    print("b is greater")
else:
    print("c is greater")

#WAP to check if number is multiple of 7 or not

value=21
if(value%7==0):
    print("Multiple by 7")
else:
    print("not multiple by 7")