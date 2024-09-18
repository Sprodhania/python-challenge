#import dependencies
import csv
import os


load_file=os.path.join("Resources","budget_data.csv")
with open(load_file) as budget_data:
    reader=csv.reader(budget_data)
    header=next(reader)
    print(header)