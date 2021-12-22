import csv

fields = []
rows = []
file_name = 'links.csv'

with open(file_name,'r') as csvfile:
    csvreader = csv.reader(csvfile)

    fields = next(csvreader)

    for row in csvreader:
        rows.append(row)
    print("Total no. of rows: %d"%(csvreader.line_num))

print("Field names are:"+','.join(field for field in fields))

for row in rows:
    for col in row:
        print("%10s"%col)
    print("\n")