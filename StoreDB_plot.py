#Use pyodbc to connect to SQL Server in python and create bar graph
import pyodbc
import matplotlib.pyplot as plt
import numpy as np

conn_str = (
    r'DRIVER={SQL Server};'
    r'SERVER=DESKTOP-DK5R027\SQLEXPRESS;'
    r'DATABASE=Store;'
    r'Trusted_Connection=yes;' )
cnxn = pyodbc.connect(conn_str)
cur = cnxn.cursor()

cur.execute("SELECT Description, Count(ORDER_LINE_ITEM.ItemNumber) AS TotalOrdered FROM ORDER_LINE_ITEM RIGHT OUTER JOIN ITEM ON ORDER_LINE_ITEM.ItemNumber = ITEM.ItemNumber GROUP BY ITEM.Description")

data = np.array(cur.fetchall())
x = data[:,0]
y = data[:,1]
plt.bar(x,y, width=.5)
plt.xticks(rotation='vertical')
plt.show()