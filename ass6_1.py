sum = lambda a,b : a + b
diff = lambda a,b : a - b
product = lambda a,b : a * b
div = lambda a,b : a / b

num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))

print("Sum is :", sum(num1,num2))
print("Difference is :", diff(num1,num2))
print("Product is :", product(num1,num2))
print("Division is :", div(num1,num2))

'''
OUTPUT:
Enter number 1 : 10
Enter number 2 : 2
Sum is : 12
Difference is : 8
Product is : 20
Division is : 5.0
'''