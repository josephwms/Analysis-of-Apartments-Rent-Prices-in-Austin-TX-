import requests
import os
import csv
import dotenv
import datetime


SOURCE_URL = "https://zillow-com1.p.rapidapi.com/propertyExtendedSearch"

dotenv.load_dotenv()
APIKEY = os.environ["APIKEY"]

#define constraints
BEDS = 2
BATHS = 2


def initial_pull():
    data = []

    '''
    There's a request limit of 2/second.  Will need to find a work-around.
    '''

    for i in range(1, 3):
        
        querystring = {"location":"Austin, TX","page":str(i),"status_type":"ForRent","home_type":"Apartments","bathsMin":"2",
                    "bathsMax":str(BEDS),"bedsMin":str(BATHS),"bedsMax":"2"}

        #Previous query contained: "sqftMin":"700","sqftMax":"1400"

        headers = {
            "X-RapidAPI-Key": APIKEY,
            "X-RapidAPI-Host": "zillow-com1.p.rapidapi.com"
        }

        response = requests.get(SOURCE_URL, headers=headers, params=querystring)

        json_ = response.json()

        data.append(json_)

    return data


def compile_and_print(raw_data, FILENAME, Print):
    data = []
    listingcount = 0
    pagecount = 0
    for dict_ in raw_data:
        pagecount = dict_['currentPage']
        subdata = dict_['props']
        listingcount += len(subdata)
        for listing in subdata:
            data.append(listing)

    if Print:
        now = datetime.datetime.now()        
        with open(FILENAME, mode="w+") as file:
            file.write(f"printed {now} +\n")
            file.write(f"there are {[pagecount]} pages and {listingcount} listings provided in this output + \n +\n")
            for d in data:
                file.write(f"{d} + \n")

    return data
    

def sum_vars(data):
    var_list = []
    for e in data:
        _vars = list(e.keys())
        if _vars not in var_list:
            var_list.append(_vars)

    
    
    # for v in var_list:
    #     print(v)
    # return


'Adding distance to uni variable.  All involving the google API was coded out by Zixuan'

def get_lat_long_by_university_name(university_name):
    
    APIKEY = os.environ["GOOGLE_APIKEY"]

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
            # print(f"Latitude: {latitude}, Longitude: {longitude}")
        else:
            print(f"Failed to retrieve coordinates. Status: {data['status']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    
    return latitude, longitude



# university_name = input("Enter the university name: ")
university_name = 'UT Austin'
la1, lo1 = get_lat_long_by_university_name(university_name)


def compute_distance(la1, la2, lo1, lo2):

    loc1 = (la1, lo1)
    loc2 = (la2, lo2)
 
    distance = round(hs.haversine(loc1, loc2, unit='mi'), 2)

    result = str(distance) + ' miles'

    return result



def return_df_relevant_vars(data):
    for info in data:
        _vars = list(info.keys())
        
        la2 = info['latitude']
        lo2 = info['longitude']

        if info['address'][-5:].isdigit():
            _zip = info['address'][-5:]
        _zip = None

        if _vars.__contains__('price'):
            price = info['price']
        price = info['units'][0]['price']
            
        info_dict = {
            'DetailURL': info['detailUrl'] 
            'Bathrooms': BEDS,
            'Bedrooms': BATHS,
            'LivingArea': info['livingArea'],
            'Price': price,
            'Rent_estimate': info['rentZestimate'],
            'Address': info['address'],
            'Zip': _zip
            'My university': university_name,
            'Distance to the university': compute_distance(la1, la2, lo1, lo2),
            'Image': info['imgSrc']
        }



if __name__ == "__main__":

    OUTPUT = "testing_vars"
    OUTPUT_DIR = "artifacts"
    FILENAME = f"{OUTPUT}.csv"

    FILEPATH = os.path.join(OUTPUT_DIR, FILENAME)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    Print = True
    raw_data = initial_pull()
    data = compile_and_print(raw_data, FILEPATH, Print)
    sum_vars(data)
