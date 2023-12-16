from geopy.distance import geodesic
import csv

csvfile = "./result_dagagu_add_distance(univ_subway).csv"
fr = open(csvfile, 'r', encoding="utf-8-sig")
rdr = csv.reader(fr)
cdb = [37.565531,126.977282]#시청역
gbd = [37.50404, 127.0469]#테헤란로
ybd = [37.5251604,126.9215586]#여의도공원
count = 0
total = 0
error = 0
for line in rdr:
    try:
        x1 = line[1]#127..
        y1 = line[0]#35..
        point_root = (x1,y1)
        point_cbd = (cdb[0],cdb[1])
        point_gbd = (gbd[0],gbd[1])
        point_ybd = (ybd[0],ybd[1])
        distance_cbd = geodesic(point_root, point_cbd).meters
        distance_gbd = geodesic(point_root, point_gbd).meters
        distance_ybd = geodesic(point_root, point_ybd).meters
        csvline = line
        csvline.insert(2,distance_ybd)
        csvline.insert(3,distance_gbd)
        csvline.insert(4,distance_cbd)
        fw = open('dagagu_add_bd.csv','a',newline='', encoding='utf-8-sig')
        wr = csv.writer(fw)
        wr.writerow(csvline)
        fw.close()
        print(f"epoch:{count},csvline:{csvline[9]}")
        count += 1
        total += 1
    except:
        print("error!")
        error += 1
        total += 1
print(f"SUCCESSFULLY COVERTED! total:{total}, error:{error}")