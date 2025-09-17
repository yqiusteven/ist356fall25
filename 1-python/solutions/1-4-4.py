'''
write a program to read in a string of students and gpas in one input statement like this:

and write out JSON like this:

```
[
    { "name" : "tom", "gpa" : 3.4 },
    { "name" : "noel", "gpa" : 3.2 },
    { "name" : "obby", "gpa" : 3.5 },
    { "name" : "peta", "gpa" : 3.4 }
]
```

Suggested approach:

    1. input text
    2. for each student split on "," from the text
    3.    split the student into name and gpa 
    4.    parse the gpa so its a float
    5.    add the name and gpa to the list
    6. write the list to students.json as JSON


'''


import json 
import os

text = input("Enter name and grades")

students = [] # empty list
for student in text.split(","): # split on comma
    name, gpa = student.strip().split() 
    gpa = float(gpa) # convert gpa to float
    students.append({"name": name, 'grade': gpa}) # add to list
print(students)

with open("students.json", "w") as file:
    json.dump(students, file, indent=2) # write to file as JSON