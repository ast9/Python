import csv
import os.path

data = []
fields = ['newtask','date']
filepath = 'todo.csv'

def open_csv():
    if os.path.isfile(filepath):
        with open(filepath,'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    
    else:
        with open(filepath,'w',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(fields)

def input_data():
    newtask = input('New Task: ')
    date = input('When: ')

    data.append({
        "newtask": newtask,
        "date": date
    })

    with open(filepath,'w',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(fields)

            for row in data:
                 writer.writerow([row['newtask'],row['date']])

open_csv()
input_data()

print(data)
