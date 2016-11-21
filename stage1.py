__author__ = 'IvyAwuor'

import requests
import json
import datetime



#-----------------Register -------------------------#
token="a4b206902a7af4fcb140c83a94910acc"
login = {'token':'a4b206902a7af4fcb140c83a94910acc', 'github':'https://github.com/rawuor/CODE2040'}
#r = requests.post("http://challenge.code2040.org/api/register", data={'token': token, 'github': 'https://github.com/rawuor/CODE2040'})
r = requests.post("http://challenge.code2040.org/api/register", data=login)
print(r.status_code, r.reason)

#--------------Step II: Reverse a string -------------------#
r = requests.post("http://challenge.code2040.org/api/reverse", data={'token':token})
print(r.status_code, r.reason)
string = r.content;
#print(string)
print("The input string is " + string)
outputstring = string[::-1]
print("Reversed string is " + outputstring)

#Send back reversed string
tokstring = {'token':token, 'string':outputstring}
r = requests.post("http://challenge.code2040.org/api/reverse/validate",data=tokstring)
print(r.status_code, r.reason)

#--------------Step III: Needle in a haystack --------------#
#grab the dictionary
r = requests.post("http://challenge.code2040.org/api/haystack", data={'token':token})
#rec = loads(urlopen(r).read())['result']
print (r.status_code, r.reason)
result = r.content
#needle =  result["needle"]
result = json.loads(r.content)
needle = result["needle"]
haystack = result["haystack"]
position = haystack.index(needle)
print(position)
resultdict = {"token":token, "needle":position}
r = requests.post("http://challenge.code2040.org/api/haystack/validate", data=resultdict)
print(r.status_code, r.reason)

#------------------Step IV: Prefix --------------------------#
#grab dictionary
r = requests.post("http://challenge.code2040.org/api/prefix", data = {"token":token})
print(r.status_code, r.reason)
result = r.json()
prefix = result["prefix"]
array = result ["array"]
temp = []

for j in range(0, len(array)):
    if array[j].startswith(prefix) == False:
        temp.append(str(array[j]))
length = len(temp)
print (length)

jsonstring = {"token":token,"array":temp}
jsonstring = json.dumps(jsonstring)
headers = {'Content-type': 'application/json'}
r = requests.post("http://challenge.code2040.org/api/prefix/validate", data=jsonstring, headers=headers)
print(r.status_code, r.reason)

#----------------Step V: Dating game -------------------------------------------#
r = requests.post("http://challenge.code2040.org/api/dating", data={"token":token})
print(r.status_code, r.reason)
result = r.json();
date = result["datestamp"]
interval = result["interval"]

print("Datestamp is " + date)
datestamp = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
datestampplus = datestamp + datetime.timedelta(0,interval)
