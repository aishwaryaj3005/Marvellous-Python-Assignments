import sys

def Freq(File, str):

    f1 = open(File, "r")
    data = f1.read()

    words = data.split()
    count = words.count(str)

    print("Frequency of ", str, "in file is :", count)

    f1.close()

def main():
    if len(sys.argv) == 3:
        File = sys.argv[1]
        str = sys.argv[2]
        Freq(File,str)
    else:
        print("Usage : python3 ass15_5  FileName  String")

if __name__ == "__main__":
    main()
    
'''
OUTPUT :
Frequency of  Marvellous in file is : 1
'''
