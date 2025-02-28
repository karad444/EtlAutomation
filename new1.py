import pyodbc

conn = pyodbc.connect(
    Trusted_connection='yes',
    Driver='{ODBC Driver 17 for SQL Server}',
    Server='SAGAR',
    Database='testing201'

)
cursor = conn.cursor()

cursor.execute("select * from testing201.dbo.emp")
for row in cursor:
    print(row)


