import requests
import csv

def get_commute_info(long,lat):
    # API URL
    api_url = "https://apis.openapi.sk.com/transit/routes/sub"
    # Headers
    headers = {
        "accept": "application/json",
        "appKey": "{삭제}",  # Replace with your actual app key
        "content-type": "application/json"
    }
    # Request parameters
    request_params = {
        "startX": f"{long}",
        "startY": f"{lat}",
        "endX": "127.0469",#teheran-ro, 
        "endY": "37.50404",#teheran-ro
        "count": 1,
        "format": "json"
    }
    # Make a POST request with headers
    response = requests.post(api_url, json=request_params, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        result = response.json()

        # Extract information from the response
        path_type = result["metaData"]["plan"]["itineraries"][0]["pathType"]
        total_time = result["metaData"]["plan"]["itineraries"][0]["totalTime"]
        transfer_count = result["metaData"]["plan"]["itineraries"][0]["transferCount"]
        total_walk_distance = result["metaData"]["plan"]["itineraries"][0]["totalWalkDistance"]
        total_distance = result["metaData"]["plan"]["itineraries"][0]["totalDistance"]
        total_fare = result["metaData"]["plan"]["itineraries"][0]["fare"]["regular"]["totalFare"]
        # Display the extracted information
        """
        print(f"Path Type: {path_type}")
        print(f"Total Time: {total_time} seconds")
        print(f"Transfer Count: {transfer_count}")
        print(f"Total Walk Distance: {total_walk_distance} meters")
        print(f"Total Distance: {total_distance} meters")
        print(f"Total Fare: {total_fare} KRW")
        """
        return {
            "sys":"SUCCESS",
            "path_type":path_type,"total_time":total_time,"transfer_count":transfer_count,
            "total_distance":total_distance,"total_walk_distance":total_walk_distance,
            "total_fare":total_fare
            }
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return {
            "sys":"ERROR",
        }

test_long = 126.9200858
test_lat = 37.6115809	

#get_commute_info(test_long,test_lat)

csvfile = "./dasedae_add_bd_fixed.csv"
fr = open(csvfile, 'r', encoding="utf-8-sig")
rdr = csv.reader(fr)

last_point = (0,0)
last_response = {}
epoch = 0
error = 0
error_api = 0
for line in rdr:
    if line[0] == "long":
        continue
    else:
        pass
    print(f"[epoch] {epoch}")
    try:
        long = line[0]
        lat = line[1]
        point = (long,lat)
        if point == last_point:
            print("pass")
            pass
        else:
            print("request")
            response = get_commute_info(str(long),str(lat))
            if response['sys'] == "ERROR":
                error_api += 1
                print("API ERROR!")
                continue
            else:
                pass
            last_point = point
            last_response = response
        gbd_path_type = last_response['path_type']
        gbd_total_time = last_response['total_time']
        gbd_transfer_count = last_response['transfer_count']
        gbd_total_distance = last_response['total_distance']
        gbd_total_walk_distance = last_response['total_walk_distance']
        gbd_total_fare = last_response['total_fare']
        csvline = line
        csvline.insert(4,gbd_path_type)
        csvline.insert(5,gbd_total_time)
        csvline.insert(6,gbd_transfer_count)
        csvline.insert(7,gbd_total_distance)
        csvline.insert(8,gbd_total_walk_distance)
        csvline.insert(9,gbd_total_fare)
        fw = open('dasedae_add_commute.csv','a',newline='', encoding='utf-8-sig')
        wr = csv.writer(fw)
        wr.writerow(csvline)
        fw.close()
        epoch += 1
        print("SUCCESS!")
    except:
        epoch += 1
        error += 1
        print("ERROR!")
print(f"epoch:{epoch}, error:{error}, api_error:{error_api}")