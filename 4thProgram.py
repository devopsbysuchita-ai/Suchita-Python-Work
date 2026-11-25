#Disctionary and Set

#Disctionary in Python:
#Dictioneries are used to store data values in key:value pairs.
#They are unordered, mutable(changeble) and don't allow duplicate keys

info = {
"Name" : "Suchita",
"Age" : 30,
"Color" : ["Green", "Yellow", "Balck", "Red"],
"Marks" : (44,55,25,96,80),
}

print(info)
print(type(info))

#if we want to print perticular key value
print(info["Name"])
print(info["Color"])

# if we want modify respective key value and we want add new key pair in dictionary

info["Age"] =29
info["Surname"]="jankar"
print(info)

#we can create empty dictionary

dict={}
print(dict)

#if we want to add key pair in empty dictionary we can do that

dict["Name"]="Omkar"
dict["Surname"]="Jankar"
print(dict)

#Nested Dictionary

student={
    "Name" : "Suchita Janakr",
    "Subject" : {
    "phy" : 98,
    "chem": 90,
    "maths": 89,
    "Bio": 90
    }
}

print (student)
print (student["Subject"]) #print nested directory
print(student["Subject"]["chem"]) # print in nested directory perticular key value

#Dictionary Methods

print(student.keys()) #returns all keys in dictionary
print(list(student.keys())) # cast in list to get a better result

print(student.values()) #returns all values in dictionary
print(list(student.values())) # cast in list to get better result

print(student.items()) #returns all key value pairs as tuple
print(list(student.items()))  # cast in list to get a better result

abc=list(student.items()) # if we want print specific key value pair then we can get this way
print(abc[0])

print(student.get("Name")) # returns the key according to the value

student.update({"City":"Pune"}) # update the disctioary
print(student)

#Set in Python:
#set is the collection of the unordered items.
#Each element in the set must be unique and immutable.

