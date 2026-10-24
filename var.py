#python variable
name = "Anuja Nandre"
age = 21
CGPA = 9.59

print("My name is: ", name)
print("My age is: ",age)
print("My CGPA is: ",CGPA)

#TYPES OF VARIABLES:
name = "Anuja Nandre"
age = 21
CGPA = 9.59

print(type(name))
print(type(age))
print(type(CGPA))


#Object References and memory management
x=10
y = x
x =20
y = 10 

print(x)
print(y)

#Deleting a variable
x = 10
y = 30
z = "Anuja"

del x 

print(y)
print(z)

 #Swapping Two Variables
a = 12
b = 24
a , b = b ,a
print(a, b)


#Counting Characters in a String:
name = "ROHAN"
length = len(name)
print("The Length of the String is: ",length)
