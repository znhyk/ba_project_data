import csv

csvfile = "./dasedae_add_commute_total.csv"
fr = open(csvfile, 'r', encoding="utf-8-sig")
rdr = csv.reader(fr)
epoch = 0
error = 0
for line in rdr:
    try:
        print(f"epoch:{epoch}")
        if line[0] == "long":
            continue
        else:
            pass
        csvline = line
        address = line[15]
        if "광진구" in address:
            goo = "gwangjin"
        elif "영등포구" in address:
            goo = "yeongdeungpo"
        elif "송파구" in address:
            goo = "songpa"
        elif "양천구" in address:
            goo = "yangcheon"
        elif "금천구" in address:
            goo = "geuncheon"
        elif "구로구" in address:
            goo = "guro"
        elif "강서구" in address:
            goo = "gangseo"
        elif "은평구" in address:
            goo = "eunpyeong"
        elif "서초구" in address:
            goo = "seocho"
        elif "강동구" in address:
            goo = "gangdong"
        elif "강남구" in address:
            goo = "gangnam"
        elif "마포구" in address:
            goo = "mapo"
        elif "서대문구" in address:
            goo = "seodaemun"
        elif "용산구" in address:
            goo = "yongsan"
        elif "노원구" in address:
            goo = "nowon"
        elif "도봉구" in address:
            goo = "donbong"
        elif "성북구" in address:
            goo = "seongbuk"
        elif "강북구" in address:
            goo = "gangbuk"
        elif "중랑구" in address:
            goo = "jungrang"
        elif "성동구" in address:
            goo = "seongdong"
        elif "동대문구" in address:
            goo = "dongdaemun"
        elif "종로구" in address:
            goo = "jongro"
        elif "중구" in address:
            goo = "jung"
        elif "동작구" in address:
            goo = "dongjak"
        elif "관악구" in address:
            goo = "gwanak"
        else:
            goo == None
        csvline.insert(15,goo)
        fw = open('dasedae_add_commute2.csv','a',newline='', encoding='utf-8-sig')
        wr = csv.writer(fw)
        wr.writerow(csvline)
        fw.close()
        epoch += 1
        #print("SUCCESS!")
    except:
        error += 1
        print(f"Error!")
print(f"COMPLETE! epoch:{epoch}, error:{error}")