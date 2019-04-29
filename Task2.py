"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def getMaxTimeRec():
    timeSpent = {}
    maxTime = 0
    maxTimeRec = ''
    for rec in calls:
        for idx in range(2):
            time = timeSpent.get(rec[idx])
            if time == None:
                timeSpent[rec[idx]] = int(rec[3])
            else:
                timeSpent.update({rec[idx]:int(time) + int(rec[3])})
                timeUpdate = timeSpent.get(rec[idx])
                if timeUpdate > maxTime:
                    maxTime = timeUpdate
                    maxTimeRec = rec[idx]
    print("{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(maxTimeRec, maxTime))

getMaxTimeRec()