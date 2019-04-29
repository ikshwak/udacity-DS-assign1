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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

def getFirstRecTexts():
    try:
        assert texts
    except AssertError:
        return None
    try:
        firstRecord = texts[0]
        return firstRecord
    except IndexError:
        return None

def printFirstRecTexts():
    firstRec = getFirstRecTexts()
    if firstRec != None:
        try:
            sender = firstRec[0]
            receiver = firstRec[1]
            time = firstRec[2]
            print("First record of texts, {0} texts {1} at time {2}".format(sender,receiver,time))
        except IndexError:
            print("missing record value(s)")
    else:
        print("First texts record not available")


printFirstRecTexts()


def getLastRecCalls():
    try:
        assert calls
    except AssertError:
        return None
    callsLen = len(calls);
    if callsLen > 0:
        return calls[callsLen-1]
    return None


def printLastRecCalls():
    lastRec = getLastRecCalls()
    if lastRec != None:
        try:
            caller = lastRec[0]
            receiver = lastRec[1]
            time = lastRec[2]
            seconds = lastRec[3]
            print("Last record of calls, {0} calls {1} at time {2}, lasting {3} seconds".format(caller,receiver,time,seconds))
        except IndexError:
            print("missing record value(s)")
    else:
        print("Last texts record not available")


printLastRecCalls()
