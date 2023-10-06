Hi guys, here is an example CSV file generated from Zillow API. 

Here is the link to the API (https://rapidapi.com/apimaker/api/zillow-com1). 

We chose 'Price', 'Living area', 'the number of bathrooms and bedrooms', and 'address' as the main attributes. You can start thinking of the methodology for analysis after having a look at the CSV file. The house data we found are from those 2B2B apartments for rent in Austin, TX. We can also find data for recently sold houses, Condos for sale, and so on by changing the parameters in the API. 

If we choose the recently sold house data, we can have the date sold, and we can conduct some simple time series analysis on it. For data of this example, we don't have the attribute time since the data are from rents of the recent month, and Zillow will not keep the data over a month for rents.

The attributes that we have added are distance to university and zip_code, for instances where the query did not yield a zip code.  These were both added using the google leapis API and the code can be referenced in the get_lat_lon.py and get_zipcode.py files.

To execute the code begin by running pip install -r requiremnts.txt in your termninal

Next, run the get_zillowData.py file using the command python3 code/get_zillowData.py