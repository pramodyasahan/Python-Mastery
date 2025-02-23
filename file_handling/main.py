import json
import os
import csv

file_path = "data/test.txt"

if os.path.exists(file_path):
    print("File exists")
else:
    print("File doesn't exist")

txt_data = "I like Juice"
file_path = "data/output.txt"

with open(file_path, "a") as file:
    file.write(txt_data)
    print("File written")

with open(file_path, "r") as file:
    data = file.read()
    print("F")

employee = {
    "name": "Spongebob",
    "age": "30",
    "job": "chef"
}

file_path = "data/output.json"
with open(file_path, "w") as file:
    json.dump(employee, file, indent=4)
    print("Json file written")

employees = [["Name", "Age", "Job"],
             ["Spongebob", 30, "Chef"],
             ["Patrick", 37, "Doctor"]]

file_path = "data/output.csv"
with open(file_path, "w") as file:
    writer = csv.writer(file)
    for employee in employees:
        writer.writerow(employee)
    print("csv file written")
