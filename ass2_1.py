import Arithmetic

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Addition:", Arithmetic.Add(num1, num2))
    print("Subtraction:", Arithmetic.Sub(num1, num2))
    print("Multiplication:", Arithmetic.Mult(num1, num2))
    print("Division:", Arithmetic.Div(num1, num2))

    if __name__ == "__main__":
        main() 
