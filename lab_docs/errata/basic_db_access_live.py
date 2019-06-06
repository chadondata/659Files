"""
Copyright 2018 Chad Harper (chad.harper@gmail.com)

Permission is hereby granted, free of charge, to any person obtaining 
a copy of this software and associated documentation files (the 
"Software"), to deal in the Software without restriction, including 
without limitation the rights to use, copy, modify, merge, publish, 
distribute, sublicense, and/or sell copies of the Software, and to 
permit persons to whom the Software is furnished to do so, subject to 
the following conditions:

The above copyright notice and this permission notice shall be 
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS 
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY 
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE 
OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""
import pyodbc
import pandas

# Connect to the server / database
use_windows_auth = True    # Change to True if you want to use integrated authentication
dsn = ' '                   # Your ODBC Data Source Name
uid = ' '                   # The SQL User ID (leave empty if windows auth)
pwd = ' '                   # The SQL Password (leave empty if windows auth)

# Dont change this:
if use_windows_auth:
    connect_string = 'DSN=%s' %(dsn)
else:
    connect_string = 'DSN=%s;UID=%s;PWD=%s' %(dsn, uid, pwd)

# Step 1: Connect to the server
conn = pyodbc.connect(connect_string)

# Step 2: Figure out your SQL
sql = " " # Enter your SQL query between the " "

# Step 2.5: Execute that SQL
data = pandas.read_sql(sql, conn)

# Step 3: Do something with whatever came back
df = pandas.DataFrame(data)

# Step 4: Show the user what they need
print(df)

# Step 5: Profit
