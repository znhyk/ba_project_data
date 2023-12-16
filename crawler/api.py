import requests

# 요청 URL
url = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"

# 필요한 정보 입력
query = "서울특별시 동대문구 답십리동 260"
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
    #"coordinate": coordinate
}

# API 요청 보내기
response = requests.get(url, params=params, headers=headers)

# 응답 확인
if response.status_code == 200:
    result = response.json()
    
    # 결과 출력
    print("Status:", result["status"])
    print("Total Count:", result["meta"]["totalCount"])
    
    if result["meta"]["totalCount"] > 0:
        address = result["addresses"][0]
        print("Road Address:", address["roadAddress"])
        print("Jibun Address:", address["jibunAddress"])
        print("English Address:", address["englishAddress"])
        print("X Coordinate:", address["x"])
        print("Y Coordinate:", address["y"])
        print("Distance:", address["distance"])
else:
    print("Error:", response.status_code, response.text)
