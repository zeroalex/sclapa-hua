import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\pessoa\Documents\sclapa-hua\COTISTAS.MDB;')
cursor = conn.cursor()
cursor.execute('select * from Agencias')
   	
for row in cursor.fetchall():
    print (row)


def pprint():
	print("old model")


#https://datatofish.com/how-to-connect-python-to-ms-access-database-using-pyodbc/