import os

def main():

    print("Enter the name of file you want to check : ")
    FileName = input()

    ret = os.path.exists(FileName)

    if(ret == True):
        print("File is present in current directory")
    else:
        print("There is no such file")


if __name__ == "__main__":
    main()

'''
OUTPUT :
Enter the name of file you want to check :
Demo.txt
There is no such file
'''