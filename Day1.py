

name = "Utkarsh"
age = 19
print(name)
print(age)
print("Hello world")
print(type(name))
print(type(age))


name = "utkarsh"
roll_no = 67
print("Name = ", name, "Roll no = ", roll_no)

name = "utkarsh"
roll_no = 67
Branch = "AI"
print("My name is {} roll no is {} and my branch is {}".format(name,roll_no,Branch))




name = "yamra"
print("Hi " + name + "!")



print("Apple","grapes","banana", sep=('-'))


print(" hello", end =(' '))
print("world")


#program to add two numbers
num1 = int(input("Enter first number"))
num2 = int(input("enter second number"))
sum = num1 + num2
print('The sum of {} and {} is {}'.format(num1,num2,sum))


#program to swap two numbers using temporary variables
num1 = int(input("enter first number"))
num2 = int(input("enetr second number"))
print("Num = {} and Num2 = {} before swapping.".format(num1,num2))
temp = num1
num1 = num2
num2 = temp
print("num1 = {} num2 = {} after swapping.".format(num1,num2))







#program to swap two numbers without using temporary variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swapping: a =", a, " b =", b)
a = a + b
b = a - b
a = a - b
print("After swapping: a =", a, " b =", b)







#program to swap using exclusive OR operator 
num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
print("Num = {} and Num 2 = {} before swapping.".format(num1,num1))
num1 = num1 ^ num2
num2 = num1 ^ num2
num1 = num1 ^ num2
print("Num 1 = {} and num2 = {} after swapping.".format(num1,num2))



#greatest of three numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 > num2 and num1 > num3:
           print("{} is greater".format(num1))
elif num2 > num3:
    print("{} is greater ".format(num2))
else:
    print("{} is greater".format(num3))



