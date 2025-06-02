import threading

def even(num):
    evensum = 0
    for i in num:
        if(i % 2 == 0):
            evensum = evensum + i
    print("Even numbers :", evensum)

def odd(num):
    oddsum = 0
    for i in num:
        if(i % 2 != 0):
            oddsum = oddsum + i
    print("Odd numbers :", oddsum)


def main():
    num = [1,2,3,4,5,6]
    print(num)

    T1 = threading.Thread(target = even, args = (num,))
    T2 = threading.Thread(target = odd, args = (num,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()

'''
OUTPUT:
[1, 2, 3, 4, 5, 6]
Even numbers : 12
Odd numbers : 9
'''