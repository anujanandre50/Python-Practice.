#Conditional Statements
#1.IF STATEMENTS
age = 20
if age >= 18:
    print("Eligible of vote.")
    
#2. IF-ELSE STATEMENT
age = 17
if age<=12:
    print("FREE TRAVELING")
else:
    print("NO FREE TRAVELLING")
    
    
#3. IF-ELIF-ELSE
age = 25

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")
    
#TRAFFIC EXAMPLE
light = "pink"
if light == "red":
    print("STOP")
elif light == "yellow":
    print('LOOK') 
elif light=="green":
    print("GO")
else:
    print("The Light is Broken")
    
    
#Grade Student based on marks
marks = int(input("Enter marks: "))
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
else:
     grade = "D"
print("Grade:", grade)


#NESTED IF
age = 70
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")