import csv

csvfile = "./dasedae_add_commute2.csv"
fr = open(csvfile, 'r', encoding="utf-8-sig")
rdr = csv.reader(fr)
epoch = 0
error = 0
for line in rdr:
    try:
        print(f"epoch:{epoch}")
        csvline = line
        if line[0] == "long":
            csvline.insert(15,"north_hangang")
            csvline.insert(16,"district")
            fw = open('dasedae_add_commute3.csv','a',newline='', encoding='utf-8-sig')
            wr = csv.writer(fw)
            wr.writerow(csvline)
            fw.close()
            epoch += 1
            continue
        else:
            pass
        address = line[16]
        if "광진구" in address:
            hansu_ebook = 1
            lebensraum = "ne"
        elif "영등포구" in address:
            hansu_ebook = 0
            lebensraum = "sw"
        elif "송파구" in address:
            hansu_ebook = 0
            lebensraum = "se"
        elif "양천구" in address:
            hansu_ebook = 0
            lebensraum = "sw"
        elif "금천구" in address:
            hansu_ebook = 0
            lebensraum = "sw"
        elif "구로구" in address:
            hansu_ebook = 0
            lebensraum = "sw"
        elif "강서구" in address:
            hansu_ebook = 0
            lebensraum = "sw"
        elif "은평구" in address:
            hansu_ebook = 1
            lebensraum = "nw" 
        elif "서초구" in address:
            hansu_ebook = 0
            lebensraum = "se"
        elif "강동구" in address:
            hansu_ebook = 0
            lebensraum = "se"
        elif "강남구" in address:
            hansu_ebook = 0
            lebensraum = "se"
        elif "마포구" in address:
            hansu_ebook = 1
            lebensraum = "nw"
        elif "서대문구" in address:
            hansu_ebook = 1
            lebensraum = "nw"
        elif "용산구" in address:
            hansu_ebook = 1
            lebensraum = "cn" 
        elif "노원구" in address:
            hansu_ebook = 1
            lebensraum = "ne"
        elif "도봉구" in address:
            hansu_ebook = 1
            lebensraum = "ne"
        elif "성북구" in address:
            hansu_ebook = 1
            lebensraum = "ne" 
        elif "강북구" in address:
            hansu_ebook = 1
            lebensraum = "ne"
        elif "중랑구" in address:
            hansu_ebook = 1
            lebensraum = "ne" 
        elif "성동구" in address:
            hansu_ebook = 1
            lebensraum = "ne" 
        elif "동대문구" in address:
            hansu_ebook = 1
            lebensraum = "ne"
        elif "종로구" in address:
            hansu_ebook = 1
            lebensraum = "cn"
        elif "중구" in address:
            hansu_ebook = 1
            lebensraum = "cn"
        elif "동작구" in address:
            hansu_ebook = 0
            lebensraum = "sw"
        elif "관악구" in address:
            hansu_ebook = 0
            lebensraum = "sw"
        else:
            hansu_ebook = None
            lebensraum = None
        csvline.insert(15,hansu_ebook)
        csvline.insert(16,lebensraum)
        fw = open('dasedae_add_commute3.csv','a',newline='', encoding='utf-8-sig')
        wr = csv.writer(fw)
        wr.writerow(csvline)
        fw.close()
        epoch += 1
        #print("SUCCESS!")
    except:
        error += 1
        print(f"Error!")
print(f"COMPLETE! epoch:{epoch}, error:{error}")