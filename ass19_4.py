import os
import sys
import shutil

def DirectoryCopy(Directory1, Directory2, Extension):

    flag = os.path.isabs(Directory1)
    if False:
        Directory1 = os.path.abspath(Directory1)

    flag = os.path.exists(Directory1)
    if False:
        print("The path is invalid")
        exit()

    flag = os.path.isdir(Directory1)
    if False:
        print("The path is valid nut th target is not directory")
        exit()

    flag = os.path.exists(Directory2)
    if False:
        os.mkdir(Directory2)

    for FolderName, SubFolderNames, FileNames in os.walk(Directory1):
        for fname in FileNames:
            if(fname.endswith(Extension)):
                file1 = os.path.join(FolderName, fname)
                relpath = os.path.relpath(FolderName, file1)
                file2 = os.path.join(Directory2, relpath)
                os.makedirs(file2, exist_ok = True)
                file2 = os.path.join(Directory2,fname)
                shutil.copy(file1, file2)
                print("Successfully Copied", file1, "to", file2)

def main():
    if(len(sys.argv) == 2):
        if(sys.argv == "--h") or (sys.argv == "--H"):
            print("this application is used to copy files from one directory to another")

        elif(sys.argv == "--u") or (sys.argv == "--U"):
            print("Use the script as :")
            print("ScriptName.py  DirectoryName1  DirectoryName2  Extension")

    elif(len(sys.argv) == 4):
        DirectoryCopy(sys.argv[1], sys.argv[2], sys.argv[3])

    else:
        print("Invalid number of commandline argument")
        print("USe the given flags as :")
        print("--h : used to display help")
        print("--u : used to display usage")

if __name__ == "__main__":
    main()