#! python3
# Selective Copy.py - walks through a folder tree and searches for files with a specified file extension.
# Copy these files from whatever location they are into a new folder in the same tree.

import os, shutil

# Walk through the folder
def selCopy(folder):
    folder = os.path.abspath(folder)  # make sure the folder is absolute

    fileType = input("Enter the filetype that you wish to copy: ")

    # Figure out the foldername this code should use based on specified extension
    copyFoldername = os.path.join(folder, "Copy of %s Files" % (fileType))
    if not os.path.exists(copyFoldername):
        os.mkdir(copyFoldername)

    # Walk through the directory
    for foldername, subfolders, filenames in os.walk(folder):

        print("The current folder is " + foldername)
        print(
            "Copying %s files from %s to %s..." % (fileType, foldername, copyFoldername)
        )

        # skip the copy folder if it exists
        if foldername == copyFoldername:
            continue

        # Copy the specified files into a folder with copyFoldername
        for filename in filenames:
            if filename.endswith(".%s" % (fileType)):
                shutil.copy(os.path.join(foldername, filename), copyFoldername)

    print("Completed.")


searchFolder = input(
    "Enter the absolute path of the folder that you wish to search in: "
)
selCopy(searchFolder)
