from geopy.distance import geodesic

# 첫 번째 지점의 위도 경도
point1 = (37.47708963, 126.9635058)  # 예시 좌표 (샌프란시스코, CA)

# 두 번째 지점의 위도 경도
point2 = (37.48702744, 127.0594749)  # 예시 좌표 (로스앤젤레스, CA)

# 두 지점 간의 거리 계산 (단위: 미터)
distance_meters = geodesic(point1, point2).meters

# 결과 출력
print(f"Distance in meters: {distance_meters} meters")
