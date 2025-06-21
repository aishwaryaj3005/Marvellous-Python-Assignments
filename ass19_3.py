import os
import sys
import shutil

def DirectoryCopy(DirectoryName1, DirectoryName2):

    flag = os.path.isabs(DirectoryName1)
    if False:
        DirectoryName1 = os.path.abspath(DirectoryName1)

    flag = os.path.exists(DirectoryName1)
    if False:
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName1)
    if False:
        print("The path is valid but the target is not directory")
        exit()

    flag = os.path.exists(DirectoryName2)
    if False:
        os.mkdir(DirectoryName2)

    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName1):
        for fname in FileNames:
            if(fname.endswith(".txt")):
                file1 = os.path.join(FolderName, fname)
                file2 = os.path.join(DirectoryName2, fname)
                shutil.copy(file1, file2)
                print("Copied", fname, "to", file2)

def main():
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h") or (sys.argv[1] == "--H"):
            print("This application is used to copy files from one directory to another")

        elif(sys.argv[1] == "--u") or (sys.argv[1] == "--U"):
            print("Use the script as :")
            print("ScriptName.py  DirectoryName1  DirectoryName2")

    elif(len(sys.argv) == 3):
        DirectoryCopy(sys.argv[1], sys.argv[2])
        
    else:
        print("Invalid number of commandline arguments")
        print("Use the given flags as :")
        print("--h : used to display help")
        print("--u : used to display usage")

if __name__ == "__main__":
    main()  