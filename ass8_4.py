import threading

def small(string):
    count = 0
    for ch in string:
        if ch.islower():
            count = count + 1
    print("\nSmall Thread")
    print("Thread ID :", threading.get_ident())
    print("Small Letters :", count)

def capital(string):
    count = 0
    for ch in string:
        if ch.isupper():
            count = count + 1
    print("\nCapital Thread")
    print("Thread ID :", threading.get_ident())
    print("Capital Letters :", count)

def digit(string):
    count = 0
    for ch in string:
        if ch.isdigit():
             count = count + 1
    print("\nDigit Thread")
    print("Thread ID :", threading.get_ident())
    print("Digits :", count)

def main():
    string = input("Enter a string : ")

    T1 = threading.Thread(target = small, args = (string,))
    T2 = threading.Thread(target = capital, args = (string,))
    T3 = threading.Thread(target = digit, args = (string,))

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()

if __name__ == "__main__":
    main()

"""
OUTPUT:
Enter a string : HeLlo123

Small Thread
Thread ID : 6176616448
Small Letters : 3

Capital Thread
Thread ID : 6193442816
Capital Letters : 2

Digit Thread
Thread ID : 6210269184
Digits : 3
"""