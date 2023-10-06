import requests
import os
import csv
import dotenv


SOURCE_URL = "https://zillow-com1.p.rapidapi.com/propertyExtendedSearch"

dotenv.load_dotenv()
APIKEY = os.environ["APIKEY"]



def initial_pull():
    data = []

    '''
    There's a request limit of 2/second.  Will need to find a work-around.
    '''

    for i in range(1, 3):
        
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

print(initial_pull())

def compile_and_print(raw_data, FILENAME):
    data = []
    listingcount = 0
    pagecount = 0
    for dict_ in raw_data:
        pagecount = dict_['currentPage']
        subdata = dict_['props']
        listingcount += len(subdata)
        for listing in subdata:
            data.append(listing)

    with open(FILENAME, mode="w+") as file:
        file.write(f"there are {[pagecount]} pages and {listingcount} listings provided in this output + \n +\n")
        for d in data:
            file.write(f"{d} + \n")

    return
    






if __name__ == "__main__":

    OUTPUT = "testing_vars"
    OUTPUT_DIR = "artifacts"
    FILENAME = f"{OUTPUT}.csv"

    FILEPATH = os.path.join(OUTPUT_DIR, FILENAME)

    os.makedirs(OUTPUT_DIR, exist_ok=True)


    raw_data = initial_pull()
    compile_and_print(raw_data, FILEPATH)
        