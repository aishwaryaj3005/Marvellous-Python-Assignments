import sys

def compare(File1, File2):
    f1 = open(File1, "r")
    f2 = open(File2, "r")

    data1 = f1.read()
    data2 = f2.read()

    if data1 == data2:
        print("Success")
    else:
        print("Failure")

    f1.close()
    f2.close()

def main():
    if len(sys.argv) == 3:
        File1 = sys.argv[1]
        File2 = sys.argv[2]
        compare(File1, File2)   
    else:
        print("Usage : python ass15_4.py  File1  File2")

if __name__ == "__main__":
    main()

'''
OUTPUT :
Failure
'''