#CREATING A LISTS
#1.Using Square Brackets:
from turtle import position


marks = [67, 89, 79, 67, 90, 39]
marks[2] = 100  
print(marks)
print(type(marks))  
print(marks[2]) 
  
#2. Using list() Constructor:
a = list((1, 2, 3, 'apple', 4.5))  
print(a)

b = list("GFG")
print(b)

#3. Creating List with Repeated Elements:
a = [2] * 5
b = [0] * 7

print(a)
print(b)

#LIST Sclicing
marks = [87, 64, 33, 95, 76]
print(marks[1:4])
print(marks[:4]) # same as marks[0:4]
print(marks[1:]) # same as marks[1:len(marks)]
print(marks[-3:-1]) # negative indexes

#3. List Methods
#1. append() - Adds an element at the end of the list
a = [1, 2]
a.append(3)
print(a)

#2. insert() - Adds an element at the specified position
a = [1, 3]
a.insert(1, 2)
print(a)

#3. extend() - Adds the elements of a list (or any iterable), to the end of the current list
a = [1, 2]
a.extend([3, 4])
print(a)



#2.Updating Elements
a = [10, 20, 30, 40, 50]
a[1] = 25 
print(a)

#Removing Elements
#1. remove(): Removes the first occurrence of an element.
a = [1, 2, 3]
a.remove(2)
print(a)

#2. pop(): Removes the element at the specified position.
a = [1, 2, 3]
a.pop()
print(a)

#3. del statement: Deletes an element at a specified index.
a = [1, 2, 3]
del a[1]
print(a)

#4. clear(): removes all items.
a = [1, 2, 3]
a.clear()
print(a)


#Iterating Over Lists
a = ['apple', 'banana', 'cherry']
for item in a:
    print(item)
    
#Nested Lists 
a = [[1, 2], [3, 4]]
print(a[0])
print(a[1][0])

#Sort in ascending order
nums = [2, 1, 3]
nums.sort()
print(nums)

#SORT(REVERSE = TRUE)-decending order
nums.sort(reverse=True)
print(nums)
nums = [2, 1, 3]


#Reverse the list
nums.reverse()
print(nums)