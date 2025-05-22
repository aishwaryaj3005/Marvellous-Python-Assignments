def prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def main():
    num = int(input("How many numbers? : "))
    numbers = []

    for i in range(num):
        numbers.append(int(input("Enter numbers : ")))
    print("List :", numbers)

    fdata = list(filter(prime, numbers))
    print("Prime numbers are :", fdata)

if __name__ == "__main__":
    main()

'''
OUTPUT:
How many numbers? : 8
Enter numbers : 10
Enter numbers : 11
Enter numbers : 12
Enter numbers : 13
Enter numbers : 14
Enter numbers : 15
Enter numbers : 16
Enter numbers : 17
List : [10, 11, 12, 13, 14, 15, 16, 17]
Prime numbers are : [11, 13, 17]
'''
