import csv  #importing the library

customer=[]
with open("data.csv") as csvFile:   #open the file
  CSVdata = csv.reader(csvFile, delimiter=',')  #read the data
  for row in CSVdata:   #loop through each row
    customer.insert(tuple(row))   #print the data
csvFile.close()   #close the file

prtint(customer)
