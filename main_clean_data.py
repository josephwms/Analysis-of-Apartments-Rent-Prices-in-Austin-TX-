import os
import dotenv
from write_csv import write_data_to_csv
from get_sorted_data import sort_data
from get_extract_data import combine_data
from get_raw_data import get_original_data

SOURCE_URL = "https://zillow-com1.p.rapidapi.com/propertyExtendedSearch"
dotenv.load_dotenv()
APIKEY = os.environ["APIKEY"]

data = get_original_data()

api_key = "AIzaSyANhM8geF0XaRYeqUu6aWhWZB4QMu1R5fA"
total_data = combine_data(data)

BASE_DIR = "artifacts"
CSV_PATH = os.path.join(BASE_DIR, "results.csv")

os.makedirs(BASE_DIR, exist_ok=True)

# sorted_data = sort_data(total_data)
write_data_to_csv(sort_data(total_data), CSV_PATH)
