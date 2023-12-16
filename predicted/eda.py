import csv

#csvfile = "./dagagu_predicted_residual(temp).csv"
csvfile = "./dasedae_predicted_residual(temp).csv"
fr = open(csvfile, 'r', encoding="cp949")
rdr = csv.reader(fr)

count = 0
for line in rdr:
    if count == 1:
        break
    else:
        pass
    for i in range(len(line)):
        print(f"{i}{line[i]}")
    count += 1