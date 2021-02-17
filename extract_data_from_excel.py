# Program to extract number
# of rows using Python
''' import xlrd
 
# Give the location of the file
loc = ("customers.xlsx")
 
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
 
# Extracting number of rows
print(sheet.nrows) '''

''' from xlrd import open_workbook
wb = open_workbook('customers.xlsx')
for s in wb.sheets():
    #print 'Sheet:',s.name
    values = []
    for row in range(s.nrows):
        col_value = []
        for col in range(s.ncols):
            value  = (s.cell(row,col).value)
            try : value = str(int(value))
            except : pass
            col_value.append(value)
        values.append(col_value)
print(values) '''

import pandas


df = pandas.read_excel("customers.xlsx",  usecols=['name', 'address'])

out = df.to_numpy().tolist()
#print(out)

out = [tuple(df) for df in out]
print(out)