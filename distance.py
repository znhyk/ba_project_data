from geopy.distance import geodesic
import csv

csvfile1 = "./지하철노선위경도정보.csv"
fr1 = open(csvfile1, 'r', encoding="cp949")
rdr1 = csv.reader(fr1)

stations = {}
for line in rdr1:
    if line[0] == "역이름":
        continue
    else:
        pass
    station = line[0]
    x = line[2]
    y = line[3]
    stations[station] = [x,y]

print(stations)

csvfile2 = "./result_dasedae.csv"
fr2 = open(csvfile2, 'r', encoding="utf-8-sig")
rdr2 = csv.reader(fr2)

csvline = []
count = 0
for line in rdr2:
    print(f"epoch:{count}")
    count += 1
    x2 = line[1]
    y2 = line[0]
    point2 = (x2,y2)
    temp_stations = stations
    for key in stations:
        xy1 = stations[key]
        x1 = xy1[0]
        y1 = xy1[1]
        point1 = (x1,y1)
        distance_meters = geodesic(point1, point2).meters
        #print(f'{key}:{distance_meters}')
        temp_stations[key].append(round(distance_meters))
    min_value_key = min(temp_stations, key=lambda k: temp_stations[k][-1])
    csvline = line
    csvline.insert(2,min_value_key)
    csvline.insert(3,temp_stations[min_value_key][-1])
    fw = open('result_dasedae_add_distance_subway.csv','a',newline='', encoding='utf-8-sig')
    wr = csv.writer(fw)
    wr.writerow(csvline)
    fw.close()