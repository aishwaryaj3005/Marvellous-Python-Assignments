num = int(input("Enter Number: "))

for i in range(num, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

'''
OUTPUT:
Enter Number: 5
* * * * * 
* * * * 
* * * 
* * 
*
'''