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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def getNumbersFromTextRecords(uniqueNumber):
    try:
        assert texts
        for rec in texts:
            if  uniqueNumber.get(rec[0]) == None:
                uniqueNumber[rec[0]] = True
            if  uniqueNumber.get(rec[1]) == None:
                uniqueNumber[rec[1]] = True
    except AssertError:
        print("no records in texts.csv")
    except IndexError:
        print("Invalid text record")

def getNumbersFromCallsRecords(uniqueNumber):
    try:
        assert calls
        for rec in calls:
            if  uniqueNumber.get(rec[0]) == None:
                uniqueNumber[rec[0]] = True
            if uniqueNumber.get(rec[1]) == None:
                uniqueNumber[rec[1]] = True
    except AssertError:
        print("no records in calls.csv")
    except IndexError:
        print("Invalid in calls record")


def printUniqueNumberCount():
    TelephoneNumbers = {}
    getNumbersFromTextRecords(TelephoneNumbers)
    getNumbersFromCallsRecords(TelephoneNumbers)
    print("There are {} different telephone numbers in the records.".format(len(TelephoneNumbers)))


printUniqueNumberCount()
