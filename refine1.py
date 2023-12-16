import csv
from datetime import datetime

#계약기간을 개월수로 변경, 없는 경우 데이터에서 제거
#
csvfile1 = "./result_dasedae_add_distance_subway.csv"
fr = open(csvfile1, 'r', encoding="utf-8-sig")
rdr = csv.reader(fr)
count = 0
for line in rdr:
    print(f'epoch{count}')
    count+=1
    csvline = line
    if line[8] == "월세" and line[17] == "-":
        continue
    else:
        pass
    monthsStr = line[17]
    print(monthsStr)
    months_diff = '-'
    if line[8] == "월세":
        start_str, end_str = monthsStr.split("~")
        # 문자열을 날짜로 변환
        start_date = datetime.strptime(start_str, "%Y%m")
        end_date = datetime.strptime(end_str, "%Y%m")
        # 년월 차이 계산
        months_diff = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
        try:
            line[12] = line[12].replace(",","")
        except:
            pass 
        junse = int(line[12])#전세보증금
        wallse = int(line[13])#월세가
        cost = junse + wallse * months_diff
    else:
        try:
            line[12] = line[12].replace(",","")
        except:
            pass 
        junse = int(line[12])#전세보증금
        wallse = int(line[13])#월세가
        cost = junse
    csvline[17] = months_diff
    csvline.insert(14,cost)
    
    fw = open('result_dasedae_refined1.csv','a',newline='', encoding='utf-8-sig')
    wr = csv.writer(fw)
    wr.writerow(csvline)
    fw.close()

"""
0:127.0602988 경도
1:37.5925342 위도
2:회기역 가장가까운 역
3:365 가장가까운 역으로부터 직선거리 m
4:서울특별시 동대문구 휘경동 187-3 구주소
5:0187 지번
6:0003  부번
7:휘경동다세대 건물이름
8:월세 전월세구분
9:41.19 제곱미터
10:202302 계약월
11:24 계약일
12:        10,000 보증금
13:            23 월세
14:2 층
15:2002 건축년도
16:이문로12길 54 신주소
17:202302~202502 계약기간
18:갱신 갱신여부
19:-
20:10,000
21:20
"""