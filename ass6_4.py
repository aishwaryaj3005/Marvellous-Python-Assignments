n1 = int(input("Enter number 1 : "))
n2 = int(input("Enter number 2 : "))
n3 = int(input("Enter number 3 : "))

if(n1 >= n2):
    if(n1 >= n3):
        print("Largest number is :", n1)
    else:
        print("Largest number is :", n3)
else:
    if(n2 >= n3):
        print("Largest number is :", n2)
    else:
        print("Largest number is :", n3)

'''
OUTput:
Enter number 1 : 5
Enter number 2 : 9
Enter number 3 : 3
Largest number is : 9
'''