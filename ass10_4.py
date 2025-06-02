from functools import reduce

product = lambda x,y : x * y

def main():
    num = int(input("How many numbers? : "))
    numbers = []

    for i in range(num):
        numbers.append(int(input("Enter numbers : ")))
    print(numbers)

    rdata = reduce(product, numbers)
    print("Product of numbers is :", rdata)

if __name__ == "__main__":
    main()

'''
OUTPUT:
How many numbers? : 3
Enter numbers : 2
Enter numbers : 3
Enter numbers : 4
[2, 3, 4]
Product of numbers is : 24
'''