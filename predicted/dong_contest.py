import csv

csvfile = "./dagagu_predicted_residual(temp).csv"
fr = open(csvfile, 'r', encoding="cp949")
rdr = csv.reader(fr)

dongDict = {}
count = 0
for line in rdr:
    if count == 0:
        count += 1
        csvline = line
        csvline.insert(19,'dong')
        fw = open('dagagu_predicted_residual(dong).csv','a',newline='', encoding='utf-8-sig')
        wr = csv.writer(fw)
        wr.writerow(csvline)
        fw.close()
        continue
    else:
        pass
    address = line[7]#다가구7:address/다세대18
    underated = int(line[36])#다가구34:under_rated/다세대46
    dong = address.split(" ")[-1]#다가구
    #dong = address.split(" ")[-2]#다세대
    if "동" not in dong:
        continue
    else:
        pass
    try:#이미 있는 경우
        dongDict[dong][0] += underated
        dongDict[dong][1] += 1
    except:#새로 만드는 경우
        dongDict[dong] = [0,0]
        dongDict[dong][0] += underated
        dongDict[dong][1] += 1
    print(dong)
    csvline = line
    csvline.insert(19,dong)
    fw = open('dagagu_predicted_residual(dong).csv','a',newline='', encoding='utf-8-sig')
    wr = csv.writer(fw)
    wr.writerow(csvline)
    fw.close()

for key in dongDict:
    underated = dongDict[key][0]
    total = dongDict[key][1]
    dongDict[key].append(underated/total)
sorted_dict = dict(sorted(dongDict.items(), key=lambda x: x[1], reverse=True))
print(sorted_dict)
for key in sorted_dict:
    csvline = sorted_dict[key]
    csvline.append(key)
    fw = open('dagagu_underated_(dong).csv','a',newline='', encoding='utf-8-sig')
    wr = csv.writer(fw)
    wr.writerow(csvline)
    fw.close()