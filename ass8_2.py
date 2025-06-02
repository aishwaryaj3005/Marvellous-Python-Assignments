import threading

def evenfactor(num):
    evensum = 0
    for i in range(1,num+1):
        if(num % i == 0 and i % 2 == 0):
            evensum = evensum + i
    print("Sum of even factors :", evensum)

def oddfactor(num):
    oddsum = 0
    for i in range(1,num+1):
        if(num % i == 0 and i % 2 != 0):
            oddsum = oddsum + i
    print("Sum of odd factors :", oddsum)


def main():
    num = int(input("Enter number : "))

    T1 = threading.Thread(target = evenfactor, args = (num,))
    T2 = threading.Thread(target = oddfactor, args = (num,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Exit from main..")

if __name__ == "__main__":
    main()

'''
OUTPUT:
Enter number : 12
Sum of even factors : 24
Sum of odd factors : 4
Exit from main..
'''