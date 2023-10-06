import requests
import os
import csv
import dotenv
import datetime
import haversine as hs
import time
#from haversine import Unit

from get_lat_lon import get_lat_long_by_university_name
from get_zipcode import get_zipcode

NOW = datetime.datetime.now()

SOURCE_URL = "https://zillow-com1.p.rapidapi.com/propertyExtendedSearch"

dotenv.load_dotenv()
APIKEY = os.environ["APIKEY"]

#define constraints
BEDS = 2
BATHS = 2
'''
API only returns 20 pages max 41 results per page.  I've kept PAGES=3 to avoid reaching the 2/second constraint
'''


def initial_pull():
    data = []

    for i in range(1, 21):
        
        querystring = {"location":"Austin, TX","page":str(i),"status_type":"ForRent","home_type":"Apartments","bathsMin":str(BATHS),
                    "bathsMax":str(BEDS),"bedsMin":str(BATHS),"bedsMax":str(BEDS)}


        headers = {
            "X-RapidAPI-Key": APIKEY,
            "X-RapidAPI-Host": "zillow-com1.p.rapidapi.com"
        }

        response = requests.get(SOURCE_URL, headers=headers, params=querystring)

        time.sleep(.25)

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
        with open(FILENAME, mode="w+") as file:
            file.write(f"printed {NOW} +\n")
            file.write(f"there are {[pagecount]} pages and {listingcount} listings provided in this output + \n +\n")
            for d in data:
                file.write(f"{d} + \n")

    return data



# university_name = input("Enter the university name: ")
university_name = 'UT Austin'
la1, lo1 = get_lat_long_by_university_name(university_name)


def compute_distance(la1, la2, lo1, lo2):
    if type(la2) == float and type(lo2) == float:

        loc1 = (la1, lo1)
        loc2 = (la2, lo2)
    
        distance = round(hs.haversine(loc1, loc2, unit='mi'), 2)

        result = str(distance) + ' miles'

        return result

    else: 
        
        return None


def return_df_relevant_vars(pre_data):
    data = []

    for info in pre_data:
        _vars = list(info.keys())
        
        la2 = info['latitude']
        lo2 = info['longitude']

        if info['address'][-5:].isdigit():
            _zip = info['address'][-5:]
        else: _zip = get_zipcode(info['address'])

        if _vars.__contains__('price'):
            price = info['price']
        else: price = int(info['units'][0]['price'][1:-1].replace(',',''))
            
        info_dict = {
            'DetailURL': 'zillow.com'+info['detailUrl'],
            'Bathrooms': BEDS,
            'Bedrooms': BATHS,
            'LivingArea': info.get('livingArea', None),
            'Price': price,
            'Rent_estimate': info.get('rentZestimate', None),
            'Address': info['address'],
            'Zip': _zip,
            'My university': university_name,
            'Distance to the university': compute_distance(la1, la2, lo1, lo2),
            'Image': info['imgSrc']
        }

        data.append(info_dict)
    
    #print(data)

    return data


def output_csv(data, FILEPATH):
    fieldnames = [
        'Price',
        'Zip',
        'My university',
        'Distance to the university',
        'Address',
        'Bathrooms',
        'Bedrooms',
        'LivingArea',
        'Rent_estimate',
        'DetailURL'
    ]

    with open(FILEPATH, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        writer.writeheader()
    
        for item in data:
            writer.writerow({
                
                'Price': item['Price'],
                'Zip': item['Zip'],
                'My university': item['My university'],
                'Distance to the university': item['Distance to the university'],
                'Address': item['Address'],
                'Bathrooms': item['Bathrooms'],
                'Bedrooms': item['Bedrooms'],
                'LivingArea': item['LivingArea'],
                'Rent_estimate': item['Rent_estimate'],
                'DetailURL': item['DetailURL']
            })
    return


if __name__ == "__main__":



    OUTPUT_PRE = "pre_data"
    OUTPUT = f"data_{NOW}"

    OUTPUT_DIR = "artifacts"

    FILENAME_PRE = f"{OUTPUT_PRE}.csv"
    FILENAME = f"{OUTPUT}.csv"

    FILEPATH_PRE = os.path.join(OUTPUT_DIR, FILENAME_PRE)
    FILEPATH = os.path.join(OUTPUT_DIR, FILENAME)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    Print = True
    raw_data = initial_pull()
    pre_data = compile_and_print(raw_data, FILEPATH_PRE, Print)
    data = return_df_relevant_vars(pre_data)
    
    output_csv(data,FILEPATH)
    
    


