import datetime
import time
import logging

#log the info
logging.basicConfig(level=logging.INFO)
logging.info("Script is running")

start = time.time()
#FileObjects
#list created to store names
listForNames= []
#Open the file
with open('names.txt', 'r') as viewFile:
    #read the names from file and convert to lowercase
    listForNames= viewFile.read().replace(" ", "_").lower().split()
    print(listForNames)

#To concatinate the domain name
def addDomainName(names):
    return names + "@pydemo.com"

#docstrings
print(addDomainName.__doc__)
#map function to update the email list
updatedNamesList = list(map(addDomainName, listForNames))
#print(updatedNamesList)

#To remove the duplicates from the updated list
remDup_updatedNamesList= list(set(updatedNamesList))
print(remDup_updatedNamesList)

#Open the text file namesupdated and write modified list to it
with open('namesupdated', 'w') as f2:
    for namesupdated in remDup_updatedNamesList:
        f2.write(namesupdated+ '\n')

#Date and time taken to execute script
print("Date and Time Stamp of execution :", datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
print("Time taken by the script to execute in Seconds is:", time.time() - start)

logging.info("Script execution is Completed")








