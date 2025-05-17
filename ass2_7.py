num = int(input("Enter number: "))

for i in range(num):
    for j in range(1, num+1):
        print(j, end = " ")
    print()

'''
OUTPUT:
Enter number: 5
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5
'''