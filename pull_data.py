import requests
import os
import dotenv
import csv

#To output data to a different file so as to not overwrite previous, change OUTPUT
OUTPUT = "Out1"


'''
create a .env file in parent directory in your local containing text "APIKEY={APIKEY}", reach out to me [Joe] if unable to find.  
Or, create own at "https://rapidapi.com/s.mahmoud97/api/zillow56"

Note: we are only allowed 30 requests per RapidAPI plan- will reevaluate if we reach the limit
'''
parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
dotenv.load_dotenv(os.path.join(parent_dir, '.env'))
APIKEY = os.environ["APIKEY"]


#LOCATION: this should be a lowercase string of form "{city}, {state code}"
LOCATION = "austin, tx"

#STATUS: 'forSale' 'forRent' or 'recentlySold'
STATUS = "recentlySold"

BASEURL = "https://zillow56.p.rapidapi.com/search"
querystring = {
    "location":LOCATION,
    "status":STATUS
}
headers = {
	"X-RapidAPI-Key": APIKEY,
	"X-RapidAPI-Host": "zillow56.p.rapidapi.com"
}

def get_response():
    response = requests.get(BASEURL, headers=headers, params=querystring)
    dry_response = response.json()

    return dry_response


def sum_data(data):
    data = dry_response["results"]
    
    perpage = dry_response["resultsPerPage"]
    pagecount= dry_response["totalPages"]
    result_total= dry_response["totalResultCount"]

    actual_total = len(data)

    print(f"perpage = {perpage}, pagecount = {pagecount}, result_total={result_total}, actual_total={actual_total}")

    return


def write_data(dry_response, path):
    data = dry_response["results"]

    with open(path, mode="w+") as file:
        for d in data:
            file.write(f"{d} + \n")

    return

if __name__ == "__main__":
    
    OUTPUT_DIR = "sandbox"
    FILENAME = f"{OUTPUT}.csv"
    #See OUTPUT on line 7

    FILEPATH = os.path.join(OUTPUT_DIR, FILENAME)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    dry_response = get_response()

    write_data(dry_response,FILEPATH)
    sum_data(dry_response)