import csv
import os
file=os.path.join("cereal.csv")
with open(file,"r",encoding="UTF-8") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    header=next(csvreader)
    print(f"the header is: {header}")
    for row in csvreader:
        if float(row[7])>=5:
            print(row)