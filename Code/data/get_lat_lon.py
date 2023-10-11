import requests
import dotenv
import os

dotenv.load_dotenv()
APIKEY = os.environ["GOOGLE_APIKEY"]

def get_lat_long_by_university_name(university_name):

    # Construct the API request URL
    base_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
    params = {
        "input": university_name,
        "inputtype": "textquery",
        "fields": "geometry/location",
        "key": APIKEY
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200 and data["status"] == "OK":
            location = data["candidates"][0]["geometry"]["location"]
            latitude = location["lat"]
            longitude = location["lng"]
            return latitude, longitude
        else:
            print(f"Failed to retrieve coordinates. Status: {data['status']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")