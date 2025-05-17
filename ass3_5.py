import MarvellousNum

def listPrime():
    n = int(input("How many numbers: "))
    numbers = []

    for i in range(n):
        numbers.append(int(input("Enter numbers: ")))

    prime_sum = 0
    for num in numbers:
        if MarvellousNum.chkPrime(num):
             prime_sum += num
        
    print("Sum of prime numbers is:", prime_sum)

listPrime()
    
'''
OUTPUT:
How many numbers: 11
Enter numbers: 13
Enter numbers: 5
Enter numbers: 45
Enter numbers: 7
Enter numbers: 4
Enter numbers: 56
Enter numbers: 10
Enter numbers: 34
Enter numbers: 2
Enter numbers: 5
Enter numbers: 8
Sum of prime numbers is: 32
'''