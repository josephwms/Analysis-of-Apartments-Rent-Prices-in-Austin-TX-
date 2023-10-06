import requests
import os
import csv
import dotenv


SOURCE_URL = "https://zillow-com1.p.rapidapi.com/propertyExtendedSearch"

dotenv.load_dotenv()
APIKEY = os.environ["APIKEY"]



def get_original_data():
    
    data = []

    '''
    There's a request limit of 2/second.  Will need to find a work-around.
    '''

    for i in range(1, 11):
        
        querystring = {"location":"Austin, TX","page":str(i),"status_type":"ForRent","home_type":"Apartments","bathsMin":"2",
                    "bathsMax":"2","bedsMin":"2","bedsMax":"2"}

        #Previous query contained: "sqftMin":"700","sqftMax":"1400"

        headers = {
            "X-RapidAPI-Key": APIKEY,
            "X-RapidAPI-Host": "zillow-com1.p.rapidapi.com"
        }

        response = requests.get(SOURCE_URL, headers=headers, params=querystring)

        json_ = response.json()

        data.append(json_)

    return data

