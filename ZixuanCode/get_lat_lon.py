import requests

def get_lat_long_by_university_name(university_name, api_key):
    # Define your Google Places API key

    # Construct the API request URL
    base_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
    params = {
        "input": university_name,
        "inputtype": "textquery",
        "fields": "geometry/location",
        "key": api_key
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200 and data["status"] == "OK":
            location = data["candidates"][0]["geometry"]["location"]
            latitude = location["lat"]
            longitude = location["lng"]
            # print(f"Latitude: {latitude}, Longitude: {longitude}")
            return latitude, longitude
        else:
            print(f"Failed to retrieve coordinates. Status: {data['status']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# api_key = "AIzaSyANhM8geF0XaRYeqUu6aWhWZB4QMu1R5fA"