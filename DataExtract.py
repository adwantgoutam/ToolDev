import re
print "Start of script"

errorCount = 0
successCount = 0

file = open('data.txt','r+')

for line in file:
    line = line.rstrip()
    if re.search('ERROR',line):
        errorCount = errorCount + 1
    elif re.search('SUCCESS',line):
        successCount = successCount + 1

print("SUCESS:",successCount)

print("ERROR:",errorCount)

