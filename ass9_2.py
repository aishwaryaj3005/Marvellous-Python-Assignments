import multiprocessing

def square(num):
    print("Squaring :", num)
    print("Result :", num * num)

def main():
    num = [1,2,3,4,5]
    numbers = []
    
    for n in num:
        P = multiprocessing.Process(target = square, args = (num,))
        numbers.append(P)
        P.start()
    
    for P in numbers:
        P.join()

    print(numbers)
if __name__ == "__main__":
    main()