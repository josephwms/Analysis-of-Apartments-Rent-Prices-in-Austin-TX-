'''A special way to generate beatiful figures, return images that can have interactions with users (in .html file)'''

import plotly.express as px
import pandas as pd

# # Load data from the CSV file
data = pd.read_csv('artifacts/result.csv')

data.iloc[:, 3] = sorted(data.iloc[:, 3])


# Create a scatter plot
fig = px.scatter(data, x='Distance to the university (in miles)', y='Price', title='Distance to the university vs. Price')

# Customize the layout
fig.update_layout(
    xaxis_title='Distance to the university (in miles)',
    yaxis_title='Price',
    showlegend=False,  # Hide legend for a cleaner look
)

# Show the plot

fig.write_html("images/DISvsPRICE_scatter_plot.html")


'''A Normal way to generate figures'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your CSV file
data = pd.read_csv('artifacts/result.csv')

data.iloc[:, 3] = sorted(data.iloc[:, 3])

# Extract the 'Price' and 'LivingArea' columns
price = data['Price']
living_area = data['LivingArea']
distance = data['Distance to the university (in miles)']
bathroom = data['Bathrooms']
bedroom = data['Bedrooms']
zip_code = data['Zip']


# Set the style and context for the plot
sns.set(style='whitegrid')
sns.set_context('talk')

# Create a line plot with 'Price' on the y-axis and 'LivingArea' on the x-axis
plt.figure(figsize=(10, 6))
sns.lineplot(x=living_area, y=price, marker='o', color='b', linewidth=2)
plt.title('Living Area vs. Price')
plt.xlabel('Living Area')
plt.ylabel('Price')

# Show the line plot
plt.savefig('images/Price_Area.png')

# Create a line plot with 'Price' on the y-axis and 'Distance' on the x-axis
plt.figure(figsize=(10, 6))
sns.lineplot(x=distance, y=price, marker='o', color='b', linewidth=2)
plt.title('Distance vs. Price')
plt.xlabel('Distance to UT Austin')
plt.ylabel('Price')
plt.savefig('images/Price_Distance.png')

# Create a line plot with 'Price' on the y-axis and 'bathroom' on the x-axis
plt.figure(figsize=(10, 6))
sns.lineplot(x=bathroom, y=price, marker='o', color='b', linewidth=2)
plt.title('Bathroom vs. Price')
plt.xlabel('Bathrooms')
plt.ylabel('Price')
plt.savefig('images/Price_Bathrooms.png')

# Create a line plot with 'Price' on the y-axis and 'bedroom' on the x-axis
plt.figure(figsize=(10, 6))
sns.lineplot(x=bedroom, y=price, marker='o', color='b', linewidth=2)
plt.title('Bedroom vs. Price')
plt.xlabel('Bedrooms')
plt.ylabel('Price')
plt.savefig('images/Price_Bedrooms.png')

# Create a line plot with 'Price' on the y-axis and 'Zip Code' on the x-axis
plt.figure(figsize=(10, 6))
sns.lineplot(x=zip_code, y=price, marker='o', color='b', linewidth=2)
plt.title('Zip_Code vs. Price')
plt.xlabel('Zip Code')
plt.ylabel('Price')
plt.savefig('images/Price_Zip.png')
