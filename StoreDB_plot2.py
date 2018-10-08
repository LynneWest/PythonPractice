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

cur.execute("SELECT ITEM.Description, temp.TotalOrdered*UnitCost AS TotalSales FROM ITEM INNER JOIN (	SELECT Description, COUNT(OLI.ItemNumber) AS TotalOrdered FROM ITEM LEFT OUTER JOIN ORDER_LINE_ITEM AS OLI ON OLI.ItemNumber = ITEM.ItemNumber GROUP BY ITEM.Description) AS temp ON ITEM.Description = temp.Description")

data = np.array(cur.fetchall())
x = data[:,0]
y = data[:,1]
plt.bar(x,y, width=.5)
plt.xticks(rotation='vertical')
plt.yticks([0,10,20,30,40,50,60,70,80], ['0', '$10', '$20', '$30', '$40', '$50', '$60', '$70', '$80'])
plt.title('Tool sale totals')
plt.grid(axis='y')
plt.show()