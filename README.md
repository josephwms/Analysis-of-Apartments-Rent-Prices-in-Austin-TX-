<big>**Welcome to our project!**<big>

Here is the link to the API (https://rapidapi.com/apimaker/api/zillow-com1). 

We chose 'Location' == 'Austin, TX', 'bathsMin/Max' == 2, 'bedsMin/Max' == 2, 'status' == 'ForRent', 'home_type' == 'Apartments'. For a query conducted around 6:00 pm Fri Oct 6, 2023, this yielded approximately 785 unique listings for each home type, conveniently within our query limit of 820 [20 pages of 41 observations each]. 

To execute the code, you should run the following codes from the terminal in order: 

>> git clone [github SSH]

>> cd eco395m-project1-midterm

>> cd Code  

>> pip install -r requirements.txt

>> python3 get_zillowData.py

>> cd ..

>> python3 Code/RF_train.py


There is a hidden .env file in the root directory and the /code directory with API keys for both the Google Maps and Zillow API. If you are receiving errors please reach out to me at joewlimms1221@gmail.com and I will share the API keys with you as they are under a paywall.

The attributes that we have added are distance to university and zip_code, for instances where the address provided in the query did not yield a zip code.  These were both added using the Google leapis API and the code can be referenced in the get_lat_lon.py and get_zipcode.py files.  


You will get a CSV file for each type of home, and also a final result.csv containing the data of all types of home.

To see data pre-cleaning and added attributes see 'pre_data.csv' in the 'artifacts' dir..  There are also page counts and observation counts from the APU query.  If you are wondering why attributes such as LivingArea and RentEstimate are missing, check that file to verify it is not included.  It may be possible to hard code some of those values using the provided link to the Zillow listing.  In the case that Zip is missing, it may be a failure from the get_zipcode.py file. However, the success rate for that query is relatively high.   

<iframe src="images/LA_P_scatter_plot.html" width="800" height="600"></iframe>





