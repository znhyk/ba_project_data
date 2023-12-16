import csv

csvfile = "./dagagu_last.csv"
fr = open(csvfile, 'r', encoding="utf-8-sig")
rdr = csv.reader(fr)

count = 0
for line in rdr:
    if count == 1:
        break
    else:
        pass
    for i in range(len(line)):
        print(f"{i}{line[i]}")
    count+= 1