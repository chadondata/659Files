#!/usr/bin/python3
# -*- coding: utf-8 -*-

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
import matplotlib.pyplot as plt

print('Running...')
# Connect to the server / database
driver = '{SQL Server}'
server = '.'                # Change to your server name (ist-s-students.syr.edu for Remote Lab)
database = 'Stitch'         # Change this to your database name (IST659_M408_netid)

use_windows_auth = True     # Change to False if you don't want to use integrated authentication
uid = ' '                   # The SQL User ID (leave empty if windows auth)
pwd = ' '                   # The SQL Password (leave empty if windows auth)

auth = ''
if use_windows_auth:
    auth = 'trusted_connection=true'
else:
    auth = 'uid=%s;pwd=%s' % (uid, pwd)

connect_string = 'DRIVER=%s;SERVER=%s;DATABASE=%s;%s' % (driver, server, database, auth)
print(connect_string) # DRIVER={SQL Server};SERVER=.;DATABASE=Stitch;trusted_connection=true

# Step 1: Connect to the server
conn = pyodbc.connect(connect_string)

# Step 2: Figure out your SQL
sql = """
SELECT * FROM Stitch_StitchPost
 """    # Enter your SQL query between the """ """

# Step 2.5: Execute that SQL
data = pandas.read_sql(sql, conn)

# Step 3: Do something with whatever came back
# 3a This line counts the number of posts per category
category_summary = data.groupby('CategoryName').agg({'StitchPostID' : 'count'})

# 3b Make a chart out of the summary (bar chart)
category_chart = category_summary.plot.bar(rot=0)

# 3c Show the chart
plt.show()


# Step 4: Show the user what they need
print(category_summary)

# Step 5: Profit
