def sum_of_digit(n):
    total = 0
    for i in str(abs(n)):
        total += int(i)
    return total

def main():
    num = int(input("Enter number: "))
    print("Sum of Digits is: ", sum_of_digit(num))

if __name__ == "__main__":
    main()

'''
OUTPUT:
Enter number: 5187934
Sum of Digits is:  37
'''