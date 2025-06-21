import os
import sys

def DirectoryWatcher(DirectoryName, Extension1, Extension2):
    
    flag = os.path.isabs(DirectoryName)
    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)
    if(flag == False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName)
    if(flag == False):
        print("The path is valid but the target is not directory")
        exit()

    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            if(fname.endswith(Extension1)):
                oldfile = os.path.join(FolderName, fname)
                newfname= fname.replace(Extension1, Extension2)
                newfile = os.path.join(FolderName, newfname)
                os.rename(oldfile, newfile)
                print(oldfile, ":", newfile)
    
    print("Task done successfully..!")
    
def main():
    if(len(sys.argv) == 2):
        if(sys.argv == "--h") or (sys.argv == "--H"):
            print("This application is used to change file extension")

        elif(sys.argv == "--u") or (sys.argv == "--U"):
            print("Use the given script as : ")
            print("ScriptName.py  DirectoryName  Extension1  Extension2")

    elif(len(sys.argv) == 4):
        DirectoryWatcher(sys.argv[1], sys.argv[2], sys.argv[3])

    else:
        print("Invalid number of commandline argument")
        print("Use the given flags as : ")
        print("--h : used to display help")
        print("--u : used to display usage")

if __name__ == "__main__":
    main()
