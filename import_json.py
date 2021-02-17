import json

customer=[]
f = open('data.json',) 
data = json.load(f) 

for i in data: 
    customer.append(tuple(i.values())) 

f.close()
print(customer)
