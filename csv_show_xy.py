import csv
import re

csvfile = "./result_1126.csv"
fr = open(csvfile, 'r', encoding="utf-8-sig")
rdr = csv.reader(fr)
count = 0
keyword = ""
for line in rdr:
    category = line[3]
    if keyword in category:
        count += 1
        print(line[1])
    else:
        pass
print(f'{keyword}:{count} found!')