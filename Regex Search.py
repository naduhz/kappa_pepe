# Regex Search.py - Opens all .txt files in a folder and searches for any line that matches
# a user-supplied regular expression. Results are printed to the screen.

import os, re, sys

myDirectory = input("Enter the absolute path of the folder you wish to search in: ")
myExpression = input("Enter an expression you wish to search for: ")
regex = re.compile(myExpression, re.IGNORECASE)

registry = {}


def txtSearch(expression, directory):
    # For-loop to loop through all files in a folder
    for file in os.listdir(directory):
        # Opens .txt file, returns the entire file in a string
        if file.endswith(".txt"):
            searchFile = open(os.path.join(directory, file), encoding="utf-8")
            searchContent = searchFile.read()
            # Creating a list for all occurences of the expression
            occurrences = regex.findall(searchContent)
            # If a match is found, return the number of occurences and the filename to the registry
            if len(occurrences) >= 1:
                registry[file] = len(occurrences)
            elif len(occurrences) == 0:
                continue
    if len(registry) != 0:
        print("Search completed. These are the results: \n")
        print("-" * 5 + "Matches and occurrences" + "-" * 5 + "\n")
        # Print matches on the left and occurrences on the right
        for k, v in registry.items():
            print(k, v)

    else:
        print("Search completed. No results found. System will now exit.")
        sys.exit()


txtSearch(myExpression, myDirectory)

continueSearch = input(
    "Enter 1 to continue the search for 1 file, or any other button to continue the search for all files, or enter X to exit: "
)

if continueSearch.lower() != "x" and continueSearch.lower() == "1":
    specificMatch = {}
    # Input the file name
    filename = input(
        "Enter the exact text file with extension which you wish to find specific matches for: "
    )
    # Check if extension is appended or if file is text
    while filename.endswith(".txt") == False:
        filename = input(
            "Either that is not a text file, or there is no extension. Please try again, or enter X to exit: "
        )
        if filename.lower() == "x":
            sys.exit()
    # Check if file exists
    if os.path.exists(os.path.join(myDirectory, filename)) != True:
        filename = input(
            "This file does not exist. Please try again, or enter X to exit: "
        )
        if filename.lower() == "x":
            sys.exit()
    # Check if file exists in registry.
    elif filename not in registry:
        filename = input(
            "This file does not have any matches. Please try again, or enter X to exit: "
        )
        if filename.lower() == "x":
            sys.exit()
    else:
        # Opens .txt file, returns the file as a list of strings
        matchFile = open(os.path.join(myDirectory, filename), encoding="utf-8")
        matchContent = matchFile.readlines()
        # Loop through the lines
        for line in matchContent:
            # Do a regex search. If a match is found, create a key-value pair in specificMatch.
            if regex.search(line) != None:
                specificMatch["Line " + str(matchContent.index(line))] = line
        print("Search completed. These are the results: \n")
        print("-" * 5 + "Matches in " + filename + "-" * 5 + "\n")
        for k, v in specificMatch.items():
            print(k, v)

elif continueSearch.lower() != "x" and continueSearch.lower() != "1":
    # Run through each text file that have already been identified.
    print("Search completed. These are the results: \n")
    for key in list(registry.keys()):
        matchFile = open(os.path.join(myDirectory, key), encoding="utf-8")
        matchContent = matchFile.readlines()
        # Create a dictionary to store the key-value pairs for that particular text file.
        tempDict = {}
        # Loop through the lines
        for line in matchContent:
            # Do a regex search. If a match is found, create a key-value pair in the temporary dictionary.
            if regex.search(line) != None:
                tempDict["Line " + str(matchContent.index(line))] = line
        print("-" * 5 + "Matches in " + key + "-" * 5 + "\n")
        for k, v in tempDict.items():
            print(k, v)
        print("\n")

else:
    print("Program terminated. System will now exit.")
    sys.exit()