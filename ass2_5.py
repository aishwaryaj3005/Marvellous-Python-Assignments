def is_prime(num):
    if num < 2:
        print("It is Not Prime Number")
        return
    
    for i in range(2, num):
        if num % i == 0:
            print("It is Not Prime Number")
            return
    print("It is Prime Number")

num = int(input("Enter Number: "))
is_prime(num)

'''
OUTPUT:
Enter Number: 5
It is Prime Number
'''