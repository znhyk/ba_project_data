from geopy.distance import geodesic
import csv

csvfile = "./dasedae_add_bd_fixed.csv"
fr = open(csvfile, 'r', encoding="utf-8-sig")
rdr = csv.reader(fr)
centre = [37.5642135, 127.0016985]#서울중심
north = [37.715133, 127.0016985]#서울 북쪽 끝
east = [37.5642135, 127.269311]#서울 동쪽 끝
west = [37.5642135, 126.734086]#서울 서쪽 끝
south = [37.413294, 127.0016985]#서울 남쪽 끝
gwangjin = [37.5481447,127.085765]#광진구중심
yeongdeungpo = [37.5206414,126.9139239]#영등포중심
songpa = [37.5048509,127.1144708]#송파구
yangcheon = [37.5270363,126.8561354]#양천구
geumcheon = [37.4600745,126.9001525]#금천구
guro = [37.4956768,126.8581205]#구로구
gangseo = [37.5657621,126.8226558]#강서구
eunpyeong = [37.6176107,126.9227001]#은평구
seocho = [37.4769532,127.0378001]#서초구
gangdong = [37.549233,127.1464401]#강동구
gangnam = [37.4959815,127.0664088]#강남구
mapo = [37.5622933,126.9087792]#마포
seodaemun = [37.5828688,126.9356676]#서대문
yongsan = [37.5311061,126.9809422]#용산구
nowon = [37.6552597,127.0771199]#노원구
dobong = [37.6658587,127.0317954]#도봉구
seongbuk = [37.6069889,127.0232435]#성북구
gangbuk = [37.6469903,127.0147136]#강북구
jungrang = [37.5953753,127.093966]#중랑구
seongdong = [37.5506718,127.0409626]#성동구
dongdaemun = [37.5837941,127.0506879]#동대문구
jongro = [37.5991001,126.986175]#종로구
jung = [37.5579449,126.9941953]#중구
dongjak = [37.4965073,126.9443079]#동작구
gwanak = [37.4654,126.9438067]#관악구

count = 0
total = 0
error = 0
for line in rdr:
    try:
        x1 = line[1]#127..
        y1 = line[0]#35..
        point_root = (x1,y1)
        #서울중앙
        point_c = (centre[0],centre[1])
        #서울북동서남
        point_n = (north[0],north[1])
        point_e = (east[0],east[1])
        point_w = (west[0],west[1])
        point_s = (south[0],south[1])
        #서울각구중심
        point_gwangjin = (gwangjin[0],gwangjin[1])
        point_yeondeungpo = (yeongdeungpo[0],yeongdeungpo[1])
        point_songpa = (songpa[0],songpa[1])
        point_yangcheon = (yangcheon[0],yangcheon[1])
        point_geumcheon = (geumcheon[0],geumcheon[1])
        point_guro = (guro[0],guro[1])
        point_gangseo = (gangseo[0],gangseo[1])
        point_eunpyeong = (eunpyeong[0],eunpyeong[1])
        point_seocho = (seocho[0],seocho[1])
        point_gangdong = (gangdong[0],gangdong[1])
        point_gangnam = (gangnam[0],gangnam[1])
        point_mapo = (mapo[0],mapo[1])
        point_seodaemun = (seodaemun[0],seodaemun[1])
        point_yongsan = (yongsan[0],yongsan[1])
        point_nowon = (nowon[0],nowon[1])
        point_dobong = (dobong[0],dobong[1])
        point_seongbuk = (seongbuk[0],seongbuk[1])
        point_gangbuk = (gangbuk[0],gangbuk[1])
        point_jungrang = (jungrang[0],jungrang[1])
        point_seongdong = (seongdong[0],seongdong[1])
        point_dongdaemun = (dongdaemun[0],dongdaemun[1])
        point_jongro = (jongro[0],jongro[1])
        point_jung = (jung[0],jung[1])
        point_dongjak = (dongjak[0],dongjak[1])
        point_gwanak = (gwanak[0],gwanak[1])
        
        
        distance_c = geodesic(point_root, point_c).meters
        distance_n = geodesic(point_root, point_n).meters
        distance_e = geodesic(point_root, point_e).meters
        distance_w = geodesic(point_root, point_w).meters
        distance_s = geodesic(point_root, point_s).meters
        
        distance_gwangjin = geodesic(point_root, point_gwangjin).meters
        distance_yeungdeungpo = geodesic(point_root, point_yeondeungpo).meters
        distance_songpa = geodesic(point_root, point_songpa).meters
        distance_yangcheon = geodesic(point_root, point_yangcheon).meters
        distance_geumcheon = geodesic(point_root, point_geumcheon).meters
        distance_guro = geodesic(point_root, point_guro).meters
        distance_gangseo = geodesic(point_root, point_gangseo).meters
        distance_eunpyeong = geodesic(point_root, point_eunpyeong).meters
        distance_seocho = geodesic(point_root, point_seocho).meters
        distance_gangdong = geodesic(point_root, point_gangdong).meters
        distance_gangnam = geodesic(point_root, point_gangnam).meters
        distance_mapo = geodesic(point_root, point_mapo).meters
        distance_seodaemun = geodesic(point_root, point_seodaemun).meters
        distance_yongsan = geodesic(point_root,point_yongsan).meters
        distance_nowon = geodesic(point_root, point_nowon).meters
        distance_dobong = geodesic(point_root, point_dobong).meters
        distance_seongbuk = geodesic(point_root, point_seongbuk).meters
        distance_gangbuk = geodesic(point_root, point_gangbuk).meters
        distance_jungrang = geodesic(point_root, point_jungrang).meters
        distance_seongdong = geodesic(point_root, point_seongdong).meters
        distance_dongdaemun = geodesic(point_root, point_dongdaemun).meters
        distance_jongro = geodesic(point_root, point_jongro).meters
        distance_jung = geodesic(point_root, point_jung).meters
        distance_dongjak = geodesic(point_root, point_dongjak).meters
        distance_gwanak = geodesic(point_root, point_gwanak).meters
        
        
        csvline = line
        csvline.insert(2,distance_c)
        csvline.insert(3,distance_n)
        csvline.insert(4,distance_e)
        csvline.insert(5,distance_w)
        csvline.insert(6,distance_s)
        csvline.insert(7,distance_gwangjin)
        csvline.insert(8,distance_yeungdeungpo)
        csvline.insert(9,distance_songpa)
        csvline.insert(10,distance_yangcheon)
        csvline.insert(11,distance_geumcheon)
        csvline.insert(12,distance_guro)
        csvline.insert(13,distance_gangseo)
        csvline.insert(14,distance_eunpyeong)
        csvline.insert(15,distance_seocho)
        csvline.insert(16,distance_gangdong)
        csvline.insert(17,distance_gangnam)
        csvline.insert(18,distance_mapo)
        csvline.insert(19,distance_seodaemun)
        csvline.insert(20,distance_yongsan)
        csvline.insert(21,distance_nowon)
        csvline.insert(22,distance_dobong)
        csvline.insert(23,distance_seongbuk)
        csvline.insert(24,distance_gangbuk)
        csvline.insert(25,distance_jungrang)
        csvline.insert(26,distance_seongdong)
        csvline.insert(27,distance_dongdaemun)
        csvline.insert(28,distance_jongro)
        csvline.insert(29,distance_jung)
        csvline.insert(30,distance_dongjak)
        csvline.insert(31,distance_gwanak)
        fw = open('dasedae_add_distances.csv','a',newline='', encoding='utf-8-sig')
        wr = csv.writer(fw)
        wr.writerow(csvline)
        fw.close()
        print(f"epoch:{count},csvline:{csvline[39]}")
        count += 1
        total += 1
    except:
        print("error!")
        error += 1
        total += 1
print(f"SUCCESSFULLY COVERTED! total:{total}, error:{error}")