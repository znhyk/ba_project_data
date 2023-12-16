import csv

csvfile = "./dagagu_last.csv"
fr = open(csvfile, 'r', encoding="utf-8-sig")
rdr = csv.reader(fr)

for line in rdr:
    long = line[0]
    lat = line[1]
    if long == "long":
        csvline = line
        fw = open('dagagu_last_fixed.csv','a',newline='', encoding='utf-8-sig')
        wr = csv.writer(fw)
        wr.writerow(csvline)
        fw.close()
        continue
    else:
        pass
    long = float(long)
    lat = float(lat)
    csvline = line
    if (126.734086 <= long <= 127.269311) and (37.413294 <= lat <= 37.715133):
        print("seoul!")
    else:
        print("not seoul!")
    