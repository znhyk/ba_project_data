import requests
import csv
def naver_api_jibun_coord(query):
    # 요청 URL
    url = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"

    # 필요한 정보 입력
    #query = "서울특별시 동대문구 답십리동 260"
    #coordinate = "127.1054328,37.3595963"
    client_id = "{삭제}"
    client_secret = "{삭제}"

    # 요청 헤더 설정
    headers = {
        "X-NCP-APIGW-API-KEY-ID": client_id,
        "X-NCP-APIGW-API-KEY": client_secret,
        "Accept": "application/json"
    }

    # 요청 파라미터 설정
    params = {
        "query": query,
        #"coordinate": coordinate #검색중심좌표로, 넣으면 해당 위치로부터의 거리가 계산됨.
    }

    # API 요청 보내기
    response = requests.get(url, params=params, headers=headers)

    # 응답 확인
    if response.status_code == 200:
        result = response.json()
        # 결과 출력
        print("Status:", result["status"])
        #print("Total Count:", result["meta"]["totalCount"])
        if result["meta"]["totalCount"] > 0:
            address = result["addresses"][0]
        else:
            return
    else:
        print("Error:", response.status_code, response.text)
    return [address["x"],address["y"]]


csvfile = "./다가구raw.csv"
fr = open(csvfile, 'r', encoding="cp949")
rdr = csv.reader(fr)
count = 0
keyword = ""
epoch = 0
omit = 0
for line in rdr:
    try:
        address = line[10]
        xjibun = address + ' 1'
        coords = naver_api_jibun_coord(xjibun)
        x = coords[0]
        y = coords[1]
        print(f"[epoch:{epoch}/omit:{omit}]success!{x},{y}:{xjibun}")
        epoch += 1
    except:
        print(f"[epoch:{epoch}/omit:{omit}]error!")
        epoch += 1
        omit += 1
        continue
    csvline = line
    csvline.insert(2, x)
    csvline.insert(3, y)
    fw = open('result_dagagu_seoul.csv','a',newline='', encoding='utf-8-sig')
    wr = csv.writer(fw)
    wr.writerow(csvline)
    fw.close()

    #workbook.save("result_excel_file.xlsx")
