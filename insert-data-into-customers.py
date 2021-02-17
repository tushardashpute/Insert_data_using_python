import mysql.connector
mydb = mysql.connector.connect(
  host="3.237.15.151",
  user="root",
  password="Sneh1#12",
  database="test"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("VamsiKrishna", "Banglore")
# mycursor.execute(sql, val)

val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

print(type(val[0]))
# mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")