# regex_search.py - Opens all .txt files in a folder and searches for any line that matches
# a user-supplied regular expression. Results are printed to the screen.

import os
import re
import sys
import argparse

parser = argparse.ArgumentParser(description='Search .txt files for a string.')
parser.add_argument('-f', '--file')
parser.add_argument('-s', '--string')
args = parser.parse_args()

if not args.file:
    myDirectory = input("Enter the absolute path of the folder you wish to search in: ")
else:
    myDirectory = args.file
if not args.string:
    myExpression = input("Enter an expression you wish to search for: ")
else:
    myExpression = args.string

regex = re.compile(myExpression, re.IGNORECASE)
registry = {}  # maps filename to number of matches
specificMatch = {}  # maps filename to matched line


def txtSearch(expression, directory):
    # For-loop to loop through all files in a folder
    for file in os.scandir(directory):
        # Opens .txt file, returns the entire file in a string
        if file.name.endswith(".txt"):
            searchFile = open(file.path, encoding="utf-8")
            searchContent = searchFile.read()
            # Creating a list for all occurences of the expression
            occurrences = regex.findall(searchContent)
            # If a match is found, return the number of occurences
            # and the filename to the registry
            if len(occurrences) >= 1:
                registry[file.name] = len(occurrences)

    if len(registry) != 0:
        print("Search completed. These are the results ( ͡°╭͜ʖ╮͡° ):\n")
        print("-" * 5 + "Matches and occurrences" + "-" * 5 + "\n")
        # Print matches on the left and occurrences on the right
        for k, v in registry.items():
            print(f'{k} - {v} occurrences')
    else:
        print("Search completed. No results found. System will now exit.")
        sys.exit()


def continueOne():
    filename = input(
        "Enter the file name for which you wish to find specific matches: "
    ).strip()
    filename += '.txt'
    while True:
        if filename not in registry:
            print('This file does not have any matches')
            next = input('Please try again, or enter X to exit: ')
            if next.lower().strip() == 'x':
                sys.exit()
            filename = next + '.txt'
            continue

        # if we reached here then a valid file was inputted
        printMatches(filename)
        break

    next = input('Select another file? Enter X to exit.')
    if next.lower().strip() == 'x':
        sys.exit()
    else:
        continueOne()


def continueAll():
    for file in registry:
        printMatches(file)


def printMatches(filename: str):
    # Opens .txt file, returns the file as a list of strings
    matchFile = open(os.path.join(myDirectory, filename), encoding="utf-8")
    matchContent = matchFile.readlines()
    # Loop through the lines
    for lineNo, line in enumerate(matchContent):
        # Do a regex search. If a match is found, create a key-value pair in specificMatch.
        hits = set(regex.findall(line))
        if hits:
            for hit in hits:
                colorfulLine = line.replace(hit, f'\x1b[1;4;31m{hit}\x1b[0m')
                specificMatch[f"Line {lineNo}"] = colorfulLine
    print("Search completed. These are the results: \n")
    print("-" * 5 + "Matches in " + filename + "-" * 5 + "\n")
    for k, v in specificMatch.items():
        print(f'{k}: {v}')
    print('\n')


if __name__ == '__main__':
    txtSearch(myExpression, myDirectory)
    continueSearch = input("Enter 1 to continue the search for 1 file, or any other button to continue the search for all files, or enter X to exit: ")
    continueSearch = continueSearch.lower().strip()
    if continueSearch == '1':
        continueOne()
    elif continueSearch == 'x':
        print("Program terminated. System will now exit.")
        sys.exit()
    else:
        continueAll()
