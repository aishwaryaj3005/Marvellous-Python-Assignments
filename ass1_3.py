def addition(no1, no2):
    ans = 0
    ans = no1 + no2
    return ans

def main():
    value1 = int(input("Enter first number: "))
    value2 = int(input("Enter second number: "))

    result = addition(value1, value2)

    print("Addition is: ", result)

if __name__ == "__main__":
    main()

'''
OUTPUT:
Enter first number: 11
Enter second number: 5
Addition is:  16
'''