def sum_of_factors(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total

def main():
    num = int(input("Enter number: "))
    print("Sum of Factors is: ", sum_of_factors(num))

if __name__ == "__main__":
    main()

'''
OUTPUT:
Enter number: 12
Sum of Factors is:  16
'''