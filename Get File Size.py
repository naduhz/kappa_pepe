#! python3

# Get File Size.py - Walks through a folder tree and searches for exceptionally large files or folders
# and prints their absolute path to the screen

import os, sys
from hurry.filesize import size

searchFolder = input("Enter the absolute folder path that you wish to search in: ")


def getFileSize(file):
    filepath = os.path.abspath(file)
    fileSize = os.path.getsize(filepath)
    return fileSize


def getFolderSize(folder):
    folderSize = 0
    folderpath = os.path.abspath(folder)
    for file in os.listdir(folderpath):
        folderSize = folderSize + os.path.getsize(os.path.join(folderpath, file))
    return folderSize


def getTreeSize(tree):
    folder = os.path.abspath(tree)  # ensure that it is a absolute folder path
    treeSize = 0
    for foldername, subfolders, filenames in os.walk(folder):

        if foldername != folder:
            print("")
            print("Current folder: " + foldername)
            print("Folder size: " + size(getFolderSize(foldername)))
            print("")
            print("Subfolders: " + str(len(subfolders)))
            for subfolder in subfolders:
                treeSize = treeSize + getFolderSize(os.path.join(foldername, subfolder))
                print(
                    subfolder
                    + " - "
                    + size(getFolderSize(os.path.join(foldername, subfolder)))
                )
            print("")
            print("Files: " + str(len(filenames)))
            for filename in filenames:
                treeSize = treeSize + getFileSize(os.path.join(foldername, filename))
                print(
                    filename
                    + " - "
                    + size(getFileSize(os.path.join(foldername, filename)))
                )

    print("\nTotal directory size: " + size(treeSize))
    return treeSize


searchFolderSize = getTreeSize(searchFolder)

while True:
    decision1 = input("Identify large files and folders? (y/n) ")
    if decision1.lower() == "y":
        break
    elif decision1.lower() == "n":
        print("System will exit.")
        sys.exit()
    else:
        print("Please try again.")


def findLargeFile(tree):
    folder = os.path.abspath(tree)  # ensure that it is a absolute folder path

    if searchFolderSize <= 100000000:
        return False
    else:
        for foldername, subfolders, filenames in os.walk(folder):
            for subfolder in subfolders:
                if getFolderSize(os.path.join(foldername, subfolder)) >= 1000000:
                    print(
                        subfolder
                        + " - "
                        + size(getFolderSize(os.path.join(foldername, subfolder)))
                    )
            for filename in filenames:
                if getFileSize(os.path.join(foldername, filename)) >= 1000000:
                    print(
                        filename
                        + " - "
                        + size(getFileSize(os.path.join(foldername, filename)))
                    )
        return True


if findLargeFile(searchFolder) != True:
    print("No results found.")