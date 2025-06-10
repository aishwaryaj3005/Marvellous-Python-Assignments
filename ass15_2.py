import os

def main():

    print("Enter the name of file : ")
    FileName = input()

    ret = os.path.exists(FileName)

    if(ret == True):
        print("File is present in current directory")

        fobj = open(FileName, "r")
        data = fobj.read()

        print("Data of the file is :", data)

        fobj.close()

    else:
        print("There is no such file")

if __name__ == "__main__":
    main()

'''
OUTPUT :
Demo.txt
File is present in current directory
Data of the file is : Hello World
'''
    