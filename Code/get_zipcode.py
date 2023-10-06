import requests
import dotenv
import os

dotenv.load_dotenv()
APIKEY = os.environ["GOOGLE_APIKEY"]

def get_zipcode(address):
    # Define the base URL for the Google Maps Geocoding API
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"

    # Parameters for the API request
    params = {
        "address": address,
        "key": APIKEY,
    }

    try:
        # Send a GET request to the API
        response = requests.get(base_url, params=params)
        data = response.json()

        # Check if the response status is OK
        if data["status"] == "OK":
            # Extract the first result's postal code
            result = data["results"][0]
            for component in result["address_components"]:
                if "postal_code" in component["types"]:
                    return component["long_name"]

        # If no zip code is found, return None
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None