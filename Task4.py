"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def createTeleMarkDict(ncTeleDict):
    """
    creates a dictionary of telemarketers who send/receive texts and receive calls
    this dictionary does not include telemarketers that make calls
    """
    try:
        for callRec in calls:
            if ncTeleDict.get(callRec[1]) == None:
                ncTeleDict[callRec[1]] = 1
    except:
        print("No call records available")

    try:
        for textRec in texts:
            if ncTeleDict.get(textRec[0]) == None:
                ncTeleDict[textRec[0]] = 1
            if ncTeleDict.get(textRec[1]) == None:
                ncTeleDict[textRec[1]] = 1
    except:
        print("No text records available")

def teleMarketers():
    """
    calls the createTeleMarkDict() to create the dictionary for non call making telemarketers
    creates a dictionary of telemarketers that meets the problem criteria.
    sorts the keys of this dictionary to display them in lexicographic order.
    enumerates through the sorted list to print them out
    """
    nonCallerTeleMarkDict = {}
    createTeleMarkDict(nonCallerTeleMarkDict)
    teleMarketerDict = {}
    try:
        for callRec in calls:
            if nonCallerTeleMarkDict.get(callRec[0]) == None and teleMarketerDict.get(callRec[0]) == None:
                teleMarketerDict[callRec[0]] = 1
        teleMarketerList = sorted(teleMarketerDict.keys())
        print("These numbers could be telemarketers: ")
        for num in teleMarketerList:
            print(num)
    except:
        print("Failed to get the telemarketer list")

teleMarketers()
