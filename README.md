Hi guys, here is an example CSV file generated from Zillow API. 

Here is the link to the API (https://rapidapi.com/apimaker/api/zillow-com1). 

We chose 'Price', 'Living area', 'the number of bathrooms and bedrooms', and 'address' as the main attributes. You can start thinking of the methodology for analysis after having a look at the CSV file. The house data we found are from those 2B2B apartments for rent in Austin, TX. We can also find data for recently sold houses, Condos for sale, and so on by changing the parameters in the API. 

If we choose the recently sold house data, we can have the date sold, and we can conduct some simple time series analysis on it. For data of this example, we don't have the attribute time since the data are from rents of the recent month, and Zillow will not keep the data over a month for rents. Also in this example, the living area is limited to 700-1400 sqft, which is a common area range for students to rent a 2B2B apartment in Austin. There are less than 100 rows in the file, but we can retrieve more data if needed, this is just an example. Also, the number of requests we can have to pull data from this API is limited, so please be careful when you run the example code. If you really wanna run the code to see the original data structure, you'd better change the value of APIKEY in the code to yours. 

There are also two attributes added by ourselves. They are 'Distance to the university' and 'My university'. I came up with the idea that we can analyze the cost of housing at different universities from different cities in the U.S. In the example code, users are allowed to type the name of their universities to check the distances from their university to the house address. We could make a comparison among various universities. Also, we can analyze these attributes of different cities by changing the location parameter. This is just a brief idea, you can think of your methodology based on it or you can find your own way.

To sum up, we can do a simple analysis of the comparison of housing prices among different cities and universities. We can also analyze the housing prices for one city. We can even simply analyze the cost-effective ratio of a university by adding functions to get the university's tuition and expected salaries after graduation.

See example codes in the template.ipynb file.
