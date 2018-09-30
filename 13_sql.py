# Работа с Базами Данных, SQL Server (PyPyODBC)
# pip install pypyodbc

import pypyodbc

connection = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=server-link;'
    'Database=db-name;'
    'uid=userName;'
    'pwd=userPass;'
)

cursor = connection.cursor()

query = (
    """
    SELECT * FROM dbo.Customers WHERE country='Canada'
    """
)

cursor.execute(query)
results = cursor.fetchall()
connection.close()

print(results)
