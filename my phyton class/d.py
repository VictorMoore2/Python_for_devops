import csv

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


data_to_write = [["name", "age"], ["Alice", 25], ["Bob", 30]]

with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data_to_write)