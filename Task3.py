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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def partA():
    try:
        assert calls
    except:
        print("No call records available")
        return
    areaCodes = {}
    for callRec in calls:
        if callRec[0].startswith('(080)'):
            if callRec[1].startswith('('):
                fixLine = callRec[1][1:callRec[1].find(')')]
                if areaCodes.get(fixLine) == None:
                    areaCodes[fixLine] = 1
            elif callRec[1].find(' ') == 5:
                mobLinePrefix = callRec[1][0:4]
                if areaCodes.get(mobLinePrefix) == None:
                    areaCodes[mobLinePrefix] = 1
    sortedAreaCodes = sorted(areaCodes.keys())
    print("The numbers called by people in Bangalore have codes:")
    for code in sortedAreaCodes:
        print(code)

partA()


def partB():
    try:
        assert calls
    except:
        print("No call records available")
        return
    outCalls = 0
    outBanCalls = 0
    for callRec in calls:
        if callRec[0].startswith('(080)'):
            outCalls +=1
            if callRec[1].startswith('(080)'):
                outBanCalls += 1
    try:
        print("{0:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format((outBanCalls/outCalls)*100))
    except ZeroDivisionError:
        print("No calls were made from fixed lines in Bangalore")

partB()
