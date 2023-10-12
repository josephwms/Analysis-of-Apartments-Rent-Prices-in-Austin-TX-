import requests
import os
import csv
import dotenv
import datetime
import haversine as hs
import time

from get_lat_lon import get_lat_long_by_university_name
from get_zipcode import get_zipcode

NOW = datetime.datetime.now()

SOURCE_URL = 'https://zillow-com1.p.rapidapi.com/propertyExtendedSearch'

dotenv.load_dotenv()
APIKEY = os.environ['APIKEY']

#define constraints
bath_bed = [[1, 1], [1, 2], [2, 2], [3, 3], [2, 4], [4, 4]]


def initial_pull(index1):
    data = []

    for i in range(1, 21):

        querystring = {
            'location': 'Austin, TX',
            'page': str(i),
            'status_type': 'ForRent',
            'home_type': 'Apartments',
            'bathsMin': str(bath_bed[index1][0]),
            'bathsMax': str(bath_bed[index1][0]),
            'bedsMin': str(bath_bed[index1][1]),
            'bedsMax': str(bath_bed[index1][1])
        }

        headers = {
            'X-RapidAPI-Key': APIKEY,
            'X-RapidAPI-Host': 'zillow-com1.p.rapidapi.com'
        }

        response = requests.get(SOURCE_URL,
                                headers=headers,
                                params=querystring)

        time.sleep(1)

        json_ = response.json()

        data.append(json_)

    return data


def compile_and_print(raw_data, FILENAME, Print):
    data = []
    listingcount = 0

    for dict_ in raw_data:
        subdata = dict_['props']
        listingcount += len(subdata)
        for listing in subdata:
            data.append(listing)

    if Print:
        with open(FILENAME, mode='w+') as file:
            file.write(f'printed {NOW} +\n')
            for d in data:
                file.write(f'{d} + \n')

    return data


university_name = 'UT Austin'
la1, lo1 = get_lat_long_by_university_name(university_name)


def compute_distance(la1, la2, lo1, lo2):
    if type(la2) == float and type(lo2) == float:

        loc1 = (la1, lo1)
        loc2 = (la2, lo2)

        distance = round(hs.haversine(loc1, loc2, unit='mi'), 2)

        result = str(distance)

        return result

    else:

        return None


def return_df_relevant_vars(pre_data, index):
    data = []

    for info in pre_data:
        _vars = list(info.keys())

        la2 = info['latitude']
        lo2 = info['longitude']

        if info['address'][-5:].isdigit():
            _zip = info['address'][-5:]
        else:
            _zip = get_zipcode(info['address'])

        if _vars.__contains__('price'):
            price = info['price']
        else:
            price = int(info['units'][0]['price'][1:-1].replace(',', ''))

        info_dict = {
            'DetailURL':
            'zillow.com' + info['detailUrl'],
            'Bathrooms':
            bath_bed[index][0],
            'Bedrooms':
            bath_bed[index][1],
            'LivingArea':
            info.get('livingArea', None),
            'Price':
            price,
            'Address':
            info['address'],
            'Zip':
            _zip,
            'My university':
            university_name,
            'Distance to the university (in miles)':
            compute_distance(la1, la2, lo1, lo2),
            'Latitude':
            la2,
            'Longitude':
            lo2,
            'Image':
            info['imgSrc']
        }

        data.append(info_dict)

    return data


def output_csv(data, FILEPATH):

    fieldnames = [
        'Price', 'Zip', 'My university',
        'Distance to the university (in miles)', 'Address', 'Bathrooms',
        'Bedrooms', 'LivingArea', 'Latitude', 'Longitude', 'DetailURL'
    ]

    with open(FILEPATH, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for item in data:
            writer.writerow({
                'Price':
                item['Price'],
                'Zip':
                item['Zip'],
                'My university':
                item['My university'],
                'Distance to the university (in miles)':
                item['Distance to the university (in miles)'],
                'Address':
                item['Address'],
                'Bathrooms':
                item['Bathrooms'],
                'Bedrooms':
                item['Bedrooms'],
                'LivingArea':
                item['LivingArea'],
                'Latitude':
                item['Latitude'],
                'Longitude':
                item['Longitude'],
                'DetailURL':
                item['DetailURL']
            })
    return


if __name__ == '__main__':

    OUTPUT_DIR = 'artifacts'

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    Print = False

    for index in range(0, len(bath_bed)):

        OUTPUT_PRE = 'pre_data_%s' % index
        OUTPUT = 'data__%s' % index

        FILENAME_PRE = f'{OUTPUT_PRE}.csv'
        FILENAME = f'{OUTPUT}.csv'

        FILEPATH_PRE = os.path.join(OUTPUT_DIR, FILENAME_PRE)
        FILEPATH = os.path.join(OUTPUT_DIR, FILENAME)

        raw_data = initial_pull(index)
        pre_data = compile_and_print(raw_data, FILEPATH_PRE, Print)
        data = return_df_relevant_vars(pre_data, index)

        output_csv(data, FILEPATH)

        print(f'Finish retrieving the {index+1}th CSV file')
    '''Combine several CSV files into one'''
    combined_data = []
    count = 0

    for filename in os.listdir(OUTPUT_DIR):
        if filename.startswith('data') and filename.endswith('.csv'):
            count += 1
            with open(os.path.join(OUTPUT_DIR, filename), 'r') as file:
                reader = csv.reader(file)
                if count > 1:
                    next(reader)  # Skip the header row if it exists
                for row in reader:
                    combined_data.append(row)

    output_file = os.path.join(OUTPUT_DIR, 'pre_result.csv')
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(combined_data)

    print(f'Finish getting pre_result.csv')
    '''Filter and keep rows with no empty values in specific columns in the CSV file'''

    input_file = os.path.join(OUTPUT_DIR, 'pre_result.csv')
    output_file = os.path.join(OUTPUT_DIR, 'result.csv')
    columns_to_check = [0, 1, 3, 7, 9, 10]

    with open(input_file,
              'r') as input_csv_file, open(output_file, 'w',
                                           newline='') as output_csv_file:
        csv_reader = csv.reader(input_csv_file)
        csv_writer = csv.writer(output_csv_file)

        for row in csv_reader:
            # Check if all specified columns are not empty
            if all(row[i] for i in columns_to_check):
                csv_writer.writerow(row)

    print(f'Finish getting result.csv')
    print(f'Success!')
