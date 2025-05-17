def main():
    n = int(input("How many numbers: "))
    numbers = []

    for i in range(n):
        numbers.append(int(input("Enter Number: ")))

    print("Min =", min(numbers))

if __name__ == "__main__":
    main()

'''
OUTPUT:
How many numbers: 4
Enter Number: 13
Enter Number: 5
Enter Number: 45
Enter Number: 7
Min = 5
'''