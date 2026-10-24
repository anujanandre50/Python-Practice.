#WAYS OF WRITTING STRING IN PYTHON
#1. Using Single Quotes
str1 = 'Hello World'

#2. Using Double Quotes
str2 = "Hello World"

#3. Using Triple Quotes
str3 = """Hello World"""

print(str1)
print(str2)
print(str3)


#STRING OPERATIONS
#a. Concatenation
str1 = "Hello"
str2 = "World"
str3 = str1  + str2  
str4 = str1 + " " +str2
print(str3)
print(str4)

#b. Length of String
str1 = "Hello"
str2 = "World"
str3 = str1  + str2  
str4 = str1 + " " +str2
print(len(str3))
print(len(str4))

#c. String Indexing
str = "DYPTC Varale"

print(str[0])
print(str[1])
print(str[2])
print(str[3])
print(str[4])
print(str[5])
print(str[6])
print(str[7])
print(str[8])
print(str[9])
print(str[10])
print(str[11])

#d. String Slicing
str = "DYPTC Varale"

print(str[0:5])
print(str[6:12])
print(str[0:12])

#Negative Indexing
s = "GUI: Tkinter"
print(s[-1])
print(s[-2])
print(s[0])
print(s[-3:-1])


#String Methods(Functions)
s = "I am learning Python"

print(s.endswith("thon"))
print(s.capitalize())
print(s.replace("Python","Java"))
print(s.find("am"))
print(s.count("a"))
print(s.upper())
print(s.lower())
print(s.startswith("I am"))
print(s.split(" "))

      
      
      

