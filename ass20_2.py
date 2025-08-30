import os
import sys
import time
import hashlib

def ChkSum(FileName):
    fobj = open(FileName, "rb")
    return hashlib.md5(fobj.read()).hexdigest()
    
def FindDup(DirectoryName):
    checksum_map = {}
    duplicates = []

    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            path = os.path.join(DirectoryName, fname)
            checksum = ChkSum(path)
            if checksum in checksum_map:
                duplicates.append(path)
            else:
                checksum_map[checksum] = path
    return duplicates

def CreateLog(Duplicate_Files):
    fobj = open("log.txt", "w")
    if not Duplicate_Files:
        fobj.write("No duplicate files found.\n")
    else:
        fobj.write("Duplicate Files:\n")
        fobj.write("=" * 20 + "\n")

        for file in Duplicate_Files:
            fobj.write(file + "\n")

    print("Log file created in current directory.")

def main():
    DirectoryName = input("Enter the name of directory : ")
    if not os.path.exists(DirectoryName):
        print("Directory does not exist")
        return
    
    duplicates = FindDup(DirectoryName)
    CreateLog(duplicates)

if __name__ == "__main__":
    main()     