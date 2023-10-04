import requests
import os
import dotenv

dotenv.load_dotenv()
APIKEY = os.environ["APIKEY"]

BASEURL = "https://zillow56.p.rapidapi.com/search"
querystring = {"location":"houston, tx","status":"recentlySold"}
headers = {
	"X-RapidAPI-Key": APIKEY,
	"X-RapidAPI-Host": "zillow56.p.rapidapi.com"
}

params = {

}

response = requests.get(BASEURL, headers=headers, params=querystring)

print(response.json())