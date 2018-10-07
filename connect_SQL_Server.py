#Use pyodbc to connect to SQL Server
import pyodbc
conn_str = (
    r'DRIVER={SQL Server};'
    r'SERVER=DESKTOP-DK5R027\SQLEXPRESS;'
    r'DATABASE=Store;'
    r'Trusted_Connection=yes;'
)
cnxn = pyodbc.connect(conn_str)
cur = cnxn.cursor()

cur.execute("SELECT * FROM CUSTOMER")
for row in cur:
  print(row)