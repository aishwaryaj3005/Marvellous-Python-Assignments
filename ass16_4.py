def Accept():
    
    num = int(input("How many numbers to enter : "))
    numbers = []

    for i in range(num):
        num = (int(input(f"Enter Number {i+1} : ")))
        numbers.append(num)
    
    fobj = open("Numbers.txt", "w")
    
    for num in numbers:
        fobj.write(str(num)+"\n")

    fobj.close()

def main():
    Accept()

if __name__ == "__main__":
    main()