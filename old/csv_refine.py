import csv
import re

for n in range(1,6+1):
    csvfile = f"./site_data{n}.csv"

    fr = open(csvfile, 'r', encoding="utf-8")
    rdr = fr.read()

    rdrList = ('"'+rdr + ', "').split('", "')
    rdrList = rdrList[1:-1]


    for i in range(0,len(rdrList),5):
        csvline = ["NA","NA","NA","NA","NA"]
        unrefined_title = rdrList[i]#정제전 타이틀
        if unrefined_title == "":
            pass
        else:
            csvline[0] = unrefined_title
        refined_title = rdrList[i+1]#정제후 타이틀
        if refined_title == "":
            pass
        else:
            csvline[1] = refined_title
        parsed_html = rdrList[i+2]#Parsed HTML Text
        try:
            parsed_html=parsed_html.replace("\n"," ")
        except:
            pass
        try:
            parsed_html=parsed_html.replace("\t"," ")
        except:
            pass
        try:
            parsed_html = re.sub(r'[^\w\s]', ' ', parsed_html)
            parsed_html = re.sub(r'\s+', ' ', parsed_html)
        except:
            pass
        if parsed_html == "":
            pass
        else:
            csvline[2] = parsed_html
        category = rdrList[i+3]#Category
        if category == "":
            pass
        else:
            csvline[3] = category
        lang = rdrList[i+4]#Language
        if lang == "한국어":
            pass
        if lang == "영어":
            pass
        else:
            lang = "기타"
        csvline[4] = lang
        print(f"epoch:[{i}]")
        fw = open('result_1201MultiLang.csv','a',newline='', encoding='utf-8-sig')
        wr = csv.writer(fw)
        wr.writerow(csvline)
        fw.close()

#공사중

#맨 처음이랑 마지막은 없음
#print(len(rdrList))
#print(rdrList[-2])