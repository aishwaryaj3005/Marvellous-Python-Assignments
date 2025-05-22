num = int(input("How many numbers? : "))
numbers = []

for i in range(num):
    numbers.append(int(input("Enter number : ")))

print("Maximum number is :",max(numbers))

'''
OUTPUT:
How many numbers? : 5
Enter number : 23
Enter number : 89
Enter number : 12
Enter number : 56
Enter number : 45
Maximum number is : 89
'''