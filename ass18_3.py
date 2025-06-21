import sys

def Copy(File):

    f1 = open(File, "r")
    f2 = open("ABC.txt", "w")

    data1 = f1.read()
    f2.write(data1)

    f1.close()
    f2.close()

    print("Data copied to ABC.txt")

def main():
    if len(sys.argv) == 2:
        File = sys.argv[1]
        Copy(File)
    else:
        print("Usage : python ass15_3.py  File")

if __name__ == "__main__":
    main()

'''
OUTPUT :
Data copied to ABC.txt
'''
    