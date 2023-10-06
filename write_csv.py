import csv

def write_data_to_csv(data, path):

    fieldnames = [
        'Price',
        'LivingArea',
        'Distance to the university',
        'Address',
        'Zip_code',
        'My university',
        'Rent_estimate',
        # 'Image',
        'Bathrooms',
        'Bedrooms'
    ]
    with open(path, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        writer.writeheader()
    
        for item in data:
            
            writer.writerow({
                'LivingArea': item['LivingArea'],
                'Price': item['Price'],
                'Distance to the university': item['Distance to the university'],
                'Address': item['Address'],
                'Zip_code': item['Zip_code'],
                'My university': item['My university'],
                'Rent_estimate': item['Rent_estimate'],
                # 'Image': item['Image'],
                'Bathrooms': item['Bathrooms'],
                'Bedrooms': item['Bedrooms']
            })
    return ''
