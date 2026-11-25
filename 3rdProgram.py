#List and Tuple in Python

#Lists in Python

#A built in datatype that stores set of values
#it can store elements of differnt types(integer, float,string etc)
#Marks = [87, 64, 33, 95, 76]         //Marks[0], Marks[1]..
#Student=["Suchita", 85, "Pune"]     //Stident[0], Student[1]..

Marks = [23,45,67,32,78,90]
print(Marks)
print(type(Marks))
print(Marks[4])
print(Marks[2])
print(len(Marks))

#String are immutable means we can't change the value which we already assign in python. 
#Lists are mutable meaning we can change the assign value in python.

#E.g

String="Hello"
print(String)
#String[0]="Hi"
#print(String) #We are getting error here as string is immutable

String1=["Suchi", 20, 44.90, 12]
print(String1)
String1[0]="Suchita" #value will be change as lists are mutable
print(String1)

#List Slicing :Similar to String Slicing

#Syntax: list_name[starting_index:ending_index]

Num=[12,45,32,67,90,23]
print(Num[3:5]) #ending index will not included o/p [67,90]
print(Num[3:]) # if we want to get list till end then no need to pass ending index o/p [67,90, 23]
print(Num[:5])

#like string slicing in list also we have negative index

print(Num[-3:-1])

#List Methods: 

list=[2,1,3]
print(list)

list.append(4) #adds one element at the end
print("Append List Method")
print(list)

list.sort() #sort ascending order
print("Sort Ascending List Method")
print(list)

list.sort(reverse=True) #sort decending order
print("Sort Dscending List Method")
print(list)

list.reverse() #reverse list
print("Reverse List Method")
print(list)

list.insert(4,5) #insert element at index syntaxt list.insert(index,element)
print("Insert Element at index List Method")
print(list)

list.remove(2) # removes first occurance of element
print("Remove List Method")
print(list)

list.pop(3) #removes element at index syntax list.pop(index)
print("Pop Method")
print(list)


#Tuples in Python
#A built in datatypes that lets us create immutable sequences of value

tup=(33,55,77,22,88)
print(tup)
#tup[0]=7 #Not allowed in python
print(type(tup))
print(tup[3])

#Tuple Slicing

print(tup[1:3])
print(tup[-3:-1])

#Tuple Method

print("Tuple Index Method")
print(tup.index(33)) #Returns index if fist occurance

print("Tuple Count Method")
print(tup.count(88)) #Counts total occurance

# Practice Questions

#WAP to ask user to enter names of their 3 favorite Movies and store them in list

Movies=[]
Mov=input("Enter First Movie name: ")
Movies.append(Mov)
Mov=input("Enter Second Movie name: ")
Movies.append(Mov)
Mov=input("Enter Third Movie name: ")
Movies.append(Mov)
print(Movies)

#WAP to check if a list contains a palindrom elements 
#Palindrom means if we read from start and end it will be laways same for eg "MAM", "racecar"
List=[1,2,3]
list_copy=List.copy()
list_copy.reverse()

if(list_copy == List):
    print("It's Plaindrom")
else:
    print("It's Not a Palindrom")

#WAP to count the number of students with the "A" grade in the following tuple

Grade=("B", "A", "C", "A", "D", "B", "A", "C", "A")
print("Count of Students with grade 'A': ", Grade.count("A"))

#WAP to store the values in a list  and sort them from accending order

Grade=["B", "A", "C", "A", "D", "B", "A", "C", "A"]
print(Grade)
Grade.sort()
print("Accending the Students Grade': ", Grade)


