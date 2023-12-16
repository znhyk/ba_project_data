from geopy.distance import geodesic
import csv

csvfile1 = "./지하철노선위경도정보.csv"
csvfile2 = "./서울시내대학위경도정보.csv"#추가필요
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
#print(stations)


fr2 = open(csvfile2, 'r', encoding="utf-8")
rdr2 = csv.reader(fr2)
univs = {}
for line in rdr2:
    univ = line[0]
    x = line[1]
    y = line[2] 
    univs[univ] = [x,y]
#print(univs)

csvfile_root = "./result_dagagu_seoul.csv"
fr_root = open(csvfile_root, 'r', encoding="utf-8-sig")
rdr_root = csv.reader(fr_root)

csvline = []
count = 0
total = 0
error = 0
for line in rdr_root:
    try:
        print(f"epoch:{count}")
        count += 1
        x2 = line[3]
        y2 = line[2]
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
        temp_univs = univs
        for key in univs:
            xy1 = univs[key]
            x1 = xy1[0]
            y1 = xy1[1]
            point1 = (x1,y1)
            distance_meters = geodesic(point1, point2).meters
            temp_univs[key].append(round(distance_meters))
        min_value_key_subway = min(temp_stations, key=lambda k: temp_stations[k][-1])
        min_value_key_univ = min(temp_univs, key=lambda k: temp_univs[k][-1])
        csvline = line
        csvline.insert(2,min_value_key_subway)
        csvline.insert(3,temp_stations[min_value_key_subway][-1])
        csvline.insert(4,min_value_key_univ)
        csvline.insert(5,temp_univs[min_value_key_univ][-1])
        fw = open('result_dagagu_add_distance(univ_subway).csv','a',newline='', encoding='utf-8-sig')
        wr = csv.writer(fw)
        wr.writerow(csvline)
        fw.close()
        total += 1
    except:
        print("error!")
        error += 1
        total += 1
print(f"SUCCESSFULLY COVERTED! total:{total}, error:{error}")