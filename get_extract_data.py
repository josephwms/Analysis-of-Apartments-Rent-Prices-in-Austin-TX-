from get_lat_lon import get_lat_long_by_university_name
from get_dis import compute_distance
from get_zipcode import get_zipcode 

def extract_json(raw_data):
    """Returns a list of all timeseries (as dict),
    given the raw data as dict."""

    json_dict = raw_data['props']
    data_list = []
    university_name = 'UT Austin'
    la1, lo1 = get_lat_long_by_university_name(university_name)
    for info in json_dict:

        if info.__contains__('price') == True and info.__contains__('livingArea') == True:
                
                la2 = info['latitude']
                lo2 = info['longitude']
                
                info_dict = {
                    'Bathrooms': 2,
                    'Bedrooms': 2,
                    'LivingArea': info['livingArea'],
                    'Price': info['price'],
                    'Rent_estimate': info['rentZestimate'],
                    'Address': info['address'],
                    'My university': university_name,
                    'Distance to the university': compute_distance(la1, la2, lo1, lo2),
                    'Zip_code': get_zipcode(info['address']),
                    'Image': info['imgSrc']
                }
                data_list.append(info_dict)

        elif info.__contains__('units') == True and info.__contains__('livingArea') == True:

            info_dict = {
                'bathrooms': 2,
                'bedrooms': 2,
                'livingArea': info['livingArea'],
                'price': info['units'][0]['price'],
                'rent_estimate': info['rentZestimate'],
                'address': info['address'],
                'My university': university_name,
                'Distance to the university': compute_distance(la1, la2, lo1, lo2),
                'Zip_code': get_zipcode(info['address']),
                'Image': info['imgSrc']
            }
        
     
    return data_list

def combine_data(data):

    total = []
    
    for raw in data:
        new = extract_json(raw)
        total.extend(new)

    return total
