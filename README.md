Welcome to our project!

Here is the link to the API (https://rapidapi.com/apimaker/api/zillow-com1). 

We chose 'Location' == 'Austin, TX', 'bathsMin/Max' == 2, 'bedsMin/Max' == 2, 'status' == 'ForRent', 'home_type' == 'Apartments'. For a query conducted around 6:00pm Fri Oct 6, 2023 this yeilded approximately 785 unique listings, conviniently within our query limit of 820 [20 pages of 41 observations each]. 

To execute the code:
(i)   run 'git clone [github SSH]' from terminal
(ii)  run 'pip install -r requiremnts.txt' from terminal
(iii) run 'code/get_zillowData.py'

There is a hidden .env file in the root directory and the /code directory with API keys for both the googlemaps and zillow API. If you are receiving errors please reach out to me at joewlimms1221@gmail.com and I will share the API keys with you as they are under paywall.

The attributes that we have added are distance to university and zip_code, for instances where the address provided in the query did not yield a zip code.  These were both added using the google leapis API and the code can be referenced in the get_lat_lon.py and get_zipcode.py files.

To see data pre cleaning and added attributes see 'pre_data.csv' in the 'artifacts' dir..  There is also page counts and obervation counts from the APU query.  If you are wondering why attributes such as LivingArea and RentEstimate are missing, check that file to verify it is not included.  It may be possible to hard code some of those values using the provided link to the Zillow listing.  In the case that Zip is missing, it may be a failure from the get_zipcode.py file.  However the successrate for that query is relatively high.





