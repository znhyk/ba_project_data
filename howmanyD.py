from geopy.distance import geodesic
import csv

csvfile = "./dasedae_add_bd_fixed.csv"
fr = open(csvfile, 'r', encoding="utf-8-sig")
rdr = csv.reader(fr)

big_list = []
for line in rdr:
    long = line[0]
    lat = line[1]
    point = (long,lat)
    big_list.append(point)

unique_list = list(set(big_list))

print(f"중복제거데이터:{len(unique_list)}")
print(unique_list[0:100])