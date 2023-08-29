import requests
import csv
import pandas as pd
import json 
import aiohttp
from schemas.serialize import serializeDict, serializeList

async def getPlaces(locationMap, query, file_name):
    
    radiusMap = 20000
    MapApiKey = "AIzaSyCmbM6cGKVeJ6wA8IoddQDgz2u1ZB9rOKE"
    print("call getPlaces")
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&location={locationMap}&radius={radiusMap}&key={MapApiKey}"
    response = requests.get(url)
    print("response : ", response)
    if response.status_code == 200:
        data = response.content  # Get the raw content of the response
        
        try:
            json_data = json.loads(data)  # Parse the content as JSON
        except json.JSONDecodeError as e:
            # Handle JSON decoding error
            return f"JSON decoding error: {e}"
        
        if json_data.get("status") == "OK":
            results = json_data.get("results", [])
            
            # Specify the CSV file path
            csv_file_path = file_name + "_data.csv"
            
            # Write data to CSV file
            with open(csv_file_path, "w", newline="", encoding="utf-8") as csv_file:
                csv_writer = csv.writer(csv_file)
                
                # Write header
                header = ["name", "address", "type", "leisure_ype", "photo_reference", "rating", "place_id"]
                csv_writer.writerow(header)
                
                # Write data rows
                for result in results:
                    name = result.get("name", "")
                    address = result.get("formatted_address", "")
                    types = ", ".join(result.get("types", []))
                    photo_reference = result.get("photos", [{}])[0].get("photo_reference", "")
                    user_ratings_total = result.get("user_ratings_total", 0)  # Set default value if None
                    place_id = result.get("place_id", "")
                    leisure_type = file_name
                    
                    # # Get latitude and longitude values
                    # location = result.get("geometry", {}).get("location", {})
                    # lat = round(location.get("lat", 0.0), 5)  # Round to 5 decimal places
                    # lng = round(location.get("lng", 0.0), 5)  # Round to 5 decimal places
                    
                    # # Convert lat and lng to strings
                    # lat_str = str(lat)
                    # lng_str = str(lng)
                    
                    # Write data to CSV file
                    csv_writer.writerow([name, address, types, leisure_type, photo_reference, user_ratings_total, place_id])
                    
            return serializeDict({"msg": "Success", "path": csv_file_path})
    print("msg", response)
    return serializeDict({"msg": response})

async def getAdventure(locationMap):
    query = "safari|hiking|surfing|water+rafting"
    file_name = "advanture"
    print('locationMap : ', locationMap)
    res = getPlaces(locationMap, query, file_name)
    print('res : ', res)
    if res != 0:
        data_frame = pd.read_csv("advanture_data.csv")
        
        # Convert DataFrame to list of dictionaries
        return data_frame

async def getShop(locationMap):
    query = "handloom+shops|tea+shops|gems+shops|handicrafts+shops|cotton+shop|shopping+mall"
    file_name = "shop"
    print('locationMap : ', locationMap)
    res = await getPlaceVisit(locationMap, query, file_name)
    
    if res != 0:
        data_frame = pd.read_csv("shop_data.csv")
        
        return data_frame
        
def concatenateAllDF():
    advanture_frame = pd.read_csv('advanture_data.csv')
    shop_frame = pd.read_csv('shop_data.csv')
    visit_frame = pd.read_csv('visit_data.csv')
    
    concatenated_df = pd.concat([advanture_frame, shop_frame, visit_frame], ignore_index=True)
    
    # Remove duplicates based on all columns
    cleaned_df = concatenated_df.drop_duplicates()

    # Save the cleaned DataFrame to a CSV file
    cleaned_df.to_csv('all_data.csv', index=False)
    
    # Convert DataFrame to list of dictionaries
    data_list = cleaned_df.to_dict(orient="records")
    return data_list

async def getPlaceVisit(locationMap, query, file_name):
    radiusMap = 20000
    MapApiKey = "AIzaSyCmbM6cGKVeJ6wA8IoddQDgz2u1ZB9rOKE"
    
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&location={locationMap}&radius={radiusMap}&key={MapApiKey}"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.text()
                
        try:
            json_data = json.loads(data)  # Parse the content as JSON
        except json.JSONDecodeError as e:
            # Handle JSON decoding error
            print("JSON decoding error:", {e})
            return f"JSON decoding error: {e}"
        
         # Serialize the JSON data
        serialized_data = json.dumps(json_data, allow_nan=False)
        # print("serialized_data", serialized_data)
        if json_data.get("status") == "OK":
            results = json_data.get("results", [])
            
            # Specify the CSV file path
            csv_file_path = file_name + "_data.csv"
            
            # Write data to CSV file
            with open(csv_file_path, "w", newline="", encoding="utf-8") as csv_file:
                csv_writer = csv.writer(csv_file)
                
                # Write header
                header = ["name", "address", "type", "leisure_ype", "photo_reference", "rating", "place_id"]
                csv_writer.writerow(header)
                
                # Write data rows
                for result in results:
                    name = result.get("name", "")
                    address = result.get("formatted_address", "")
                    types = ", ".join(result.get("types", []))
                    photo_reference = result.get("photos", [{}])[0].get("photo_reference", "no photo")
                    user_ratings_total = result.get("user_ratings_total", 0)  # Set default value if None
                    place_id = result.get("place_id", "")
                    leisure_type = file_name
                    
                    # # Get latitude and longitude values
                    # location = result.get("geometry", {}).get("location", {})
                    # lat = round(location.get("lat", 0.0), 5)  # Round to 5 decimal places
                    # lng = round(location.get("lng", 0.0), 5)  # Round to 5 decimal places
                    
                    # # Convert lat and lng to strings
                    # lat_str = str(lat)
                    # lng_str = str(lng)
                    
                    # Write data to CSV file
                    csv_writer.writerow([name, address, types, leisure_type, photo_reference, user_ratings_total, place_id])
                    
            return serializeDict({"msg": "Success", "path": csv_file_path})
    print("msg", response)
    return serializeDict({"msg": response})

async def getVisit(locationMap):
    query ="tourist+attractions"
    file_name = "visit"
    print('locationMap : ', locationMap)
    res = await getPlaceVisit(locationMap, query, file_name)
    print('res : ', res)
    if res != 0:
        data_frame = pd.read_csv("visit_data.csv")
        
        # Convert DataFrame to list of dictionaries
        return data_frame
  
# get places
async def getTypeByPlace(locationMap, query):
    res =await getPlaces(locationMap, query, "look")
    if res != 0:
        data_frame = pd.read_csv("look_data.csv")
        # get most common type from data frame
        most_common_type = data_frame['type'].value_counts().idxmax()
        print("most_common_type", most_common_type)
        return most_common_type
            
