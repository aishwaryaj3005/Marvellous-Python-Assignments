even = lambda n : n % 2 == 0

def main():
    num = int(input("How many numbers? : "))
    numbers = []

    for i in range(num):
        numbers.append(int(input("Enter numbers : ")))
    print(numbers)

    fdata = list(filter(even, numbers))
    print("Even numbers are :", fdata)

if __name__ == "__main__":
    main()

'''
OUTPUT:
How many numbers? : 6
Enter numbers : 1
Enter numbers : 2
Enter numbers : 3
Enter numbers : 4
Enter numbers : 5
Enter numbers : 6
[1, 2, 3, 4, 5, 6]
Even numbers are : [2, 4, 6]
'''