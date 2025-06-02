import threading

def even():
    print("First 10 even numbers : ")
    for i in range(2,21,2):
        print(i, end = " ")

def odd():
    print("\nFirst 10 odd numbers : ")
    for i in range(1,21,2):
        print(i, end = " ")

def main():
    T1 = threading.Thread(target = even)
    T2= threading.Thread(target = odd)

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()

'''
OUTPUT:
First 10 even numbers :
2 4 6 8 10 12 14 16 18 20 
First 10 odd numbers : 
1 3 5 7 9 11 13 15 17 19
'''