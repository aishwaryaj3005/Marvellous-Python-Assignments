def main():
    n = int(input("How many numbers: "))
    numbers = []

    for i in range(n):
        numbers.append(int(input("Enter Number: ")))
    print(numbers)
    
    search = int(input("Enter number to search: "))

    freq = numbers.count(search)
    print("Frequency of", search, "is: ", freq)

if __name__ == "__main__":
    main()

'''
OUTPUT:
How many numbers: 11
Enter Number: 13
Enter Number: 5
Enter Number: 45
Enter Number: 7
Enter Number: 4
Enter Number: 56
Enter Number: 5
Enter Number: 34
Enter Number: 2
Enter Number: 5
Enter Number: 65
[13, 5, 45, 7, 4, 56, 5, 34, 2, 5, 65]
Enter number to search: 5
Frequency of 5 is:  3
'''