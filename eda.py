import csv

csvfile1 = "./result_dasedae_add_distance_subway.csv"
fr = open(csvfile1, 'r', encoding="utf-8-sig")
rdr = csv.reader(fr)
for line in rdr:
    count=0
    for value in line:
        print(f'{count}:{value}')
        count+=1
