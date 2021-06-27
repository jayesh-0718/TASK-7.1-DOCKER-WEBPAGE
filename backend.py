#!/usr/bin/python3


import subprocess as sp
import cgi

print("content-type: text/html")
print()
print('''<style>
        pre{
        color: black;
        font-weight: bold;
        font-size: 15px;
        }
        </style>
        ''')
fs = cgi.FieldStorage()
cmd = fs.getvalue("command")
output = sp.getoutput("sudo "+cmd)

print("<body>")
print('<h1 style="color:#df405a;" >Output</h1>')
print("<pre>{}</pre>".format(output))
print("</body>")

