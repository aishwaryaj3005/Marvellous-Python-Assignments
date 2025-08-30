import os
import sys
import hashlib

def ChkSum(DirectoryName):
    flag = os.path.isabs
    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)
    if(flag == False):
        print("Invalid path")
        exit()

    flag = os.path.isdir(DirectoryName)
    if(flag == False):
        print("the path is valid but the target is not Directory")
        exit()

    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            path = os.path.join(FolderName, fname)
            fobj = open(path, "rb")
            hobj = hashlib.md5()
            buffer = fobj.read(1024)
            while(len(buffer) > 0):
                 hobj.update(buffer)
            print(f"{path} : {hobj.hexdigest()}")
        fobj.close()
        
def main():
    if(len(sys.argv) == [2]):
        if(sys.argv[1] == "--h") or (sys.argv[1] == "--H"):
            print("This application is used to check total number of files in Directory")

        elif(sys.argv[1] == "--u") or (sys.argv[1] == "--U"):
            print("Use the given script as :")
            print("ScriptName.py  DirectoryName")

    elif(len(sys.argv) == [2]):
        ChkSum(sys.argv[1])

    else:
        print("Invalid number of commandline arguments")
        print("Use the given flags as :")
        print("--h : used to display help")
        print("--u : used to display usage")

if __name__ == "__main__":
    main()