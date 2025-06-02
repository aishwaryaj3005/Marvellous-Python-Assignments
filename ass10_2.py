double = lambda n : n * 2

def main():
    num = int(input("How many numbers? : "))
    numbers = []

    for i in range(num):
        numbers.append(int(input("Enter numbers : ")))
    print(numbers)

    mdata = list(map(double, numbers))
    print("Double numbers :", mdata)

if __name__ == "__main__":
    main()

'''
OUTPUT:
How many numbers? : 5
Enter numbers : 1
Enter numbers : 2
Enter numbers : 3
Enter numbers : 4
Enter numbers : 5
[1, 2, 3, 4, 5]
Double numbers : [2, 4, 6, 8, 10]
'''