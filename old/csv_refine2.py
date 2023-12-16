import csv
import re

#csvfile = "./result_1125KoreanOnly.csv"
csvfile = "./result_1201MultiLang.csv"
fr = open(csvfile, 'r', encoding="utf-8-sig")
rdr = csv.reader(fr)
for line in rdr:
    csvline = ['','','','','']
    if line[0] == "" or line[0] == None:
        print("unrefined_title:NULL!")
        continue
    else:
        unrefined_title = line[0]
    if line[1] == "" or line[1] == None:
        print("refined_title:NULL!")
        continue
    else:
        refined_title = line[1]
    if line[2] == "" or line[2] == None:
        print("parsed_html:NULL!")
        continue
    else:
        parsed_html = line[2]
    if line[3] == "" or line[3] == None:
        print("category:NULL!")
        continue
    else:
        category = line[3]
    if line[4] == "" or line[4] == None:
        print("language:NULL!")
        continue
    else:
        language = line[4]
    print("saved!")
    csvline[0] = unrefined_title
    csvline[1] = refined_title
    csvline[2] = parsed_html
    csvline[3] = category
    csvline[4] = language
    fw = open('result_1201refined_MultiLang.csv','a',newline='', encoding='utf-8-sig')
    wr = csv.writer(fw)
    wr.writerow(csvline)
    fw.close()