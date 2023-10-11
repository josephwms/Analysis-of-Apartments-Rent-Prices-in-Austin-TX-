import pandas as pd
import folium

# Load the CSV data into a DataFrame
df = pd.read_csv('artifacts/result.csv') 

# Create a map centered on a location (UT Austin)
map_center = [30.2849 , -97.7341]  



# Create a Folium map
m = folium.Map(location=map_center, zoom_start=12)

# Iterate through the DataFrame and add markers for each data point
for index, row in df.iterrows():

    location = (row['Latitude'], row['Longitude'])
    price = row['Price']
    zip_code = row['Zip']
    living_area = row['LivingArea']
    bathroom = row['Bathrooms']
    bedroom = row['Bedrooms']
    distance = row['Distance to the university (in miles)']
    URL = row['DetailURL']

  # Replace latitude and longitude with actual coordinates for the zip code
    popup_text = f"Zip Code: {zip_code}<br>Price:${price}\
                <br>Area: {living_area} sqft.<br>Bathrooms: {bathroom}\
                <br>Bedrooms: {bedroom}<br>Dis.to Uni.: {distance} miles\
                <br>DetailURL: {URL}"
    

    # Create a marker for each data point
    folium.Marker(
        location=location,
        popup=popup_text,
        icon=folium.Icon(icon='home')
    ).add_to(m)

# Save the map to an HTML file
m.save('images/rent_price_map.html')
