import os
import sys

def DirectoryFileSearch(DirectoryName, Extension):
    flag = os.path.isabs(DirectoryName)
    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)
    
    flag = os.path.exists(DirectoryName)
    if(flag == False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName)
    if(flag == False):
        print("The path is valid but the target is not Directory")
        exit()

    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName):
            for fname in FileNames:
                fname = os.path.join(FolderName, fname)
                if(fname.endswith(Extension)):
                    print("Files are :", fname)
    
def main():
    if(len(sys.argv) == [2]):
        if(sys.argv[1] == "--h") or (sys.argv[1] == "--H"):
            print("This application is used to display files of same extension")
        
        elif(sys.argv[1] == "--u") or (sys.argv[1] == "--U"):
            print("Use the given script as :")
            print("Scriptname.py  NameofDirectory  FileExtension")
        
    elif(len(sys.argv) == 3):
        DirectoryFileSearch(sys.argv[1], sys.argv[2])
    
    else:
        print("Invalid number of commandline argument")
        print("Use the given flags as : ")
        print("--h : used to display help")
        print("--u : used to display usage")

if __name__ == "__main__":
    main()