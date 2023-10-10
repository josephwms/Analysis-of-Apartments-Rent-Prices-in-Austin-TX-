import plotly.express as px
import pandas as pd
import numpy as np
from scipy.stats import gaussian_kde
import seaborn as sns
import matplotlib.pyplot as plt


# Load data from the CSV file. Please change it to the Appropriate path.
data = pd.read_csv(r'C:\users\rayna\downloads\repos\eco395m-project1-midterm\artifacts\result.csv')

data.iloc[:, 3] = sorted(data.iloc[:, 3])

# Please Set the base path for images
image_path = r'C:\users\rayna\downloads\repos\eco395m-project1-midterm\images'

# Create a scatter plot
fig = px.scatter(data, x='Distance to the university (in miles)', y='Price', title='Distance to the university vs. Price')

# Customize the layout
fig.update_layout(
    xaxis_title='Distance to the university (in miles)',
    yaxis_title='Price',
    showlegend=False,  # Hide legend for a cleaner look
)

# Show the plot
fig.write_html(f"{image_path}\\DISvsPRICE_scatter_plot.html")



data.iloc[:, 3] = sorted(data.iloc[:, 3])

# Extract the relevant columns
price = data['Price']
living_area = data['LivingArea']
distance = data['Distance to the university (in miles)']
bathroom = data['Bathrooms']
bedroom = data['Bedrooms']
zip_code = data['Zip']

# Set the style and context for the plot
sns.set(style='whitegrid')
sns.set_context('talk')

#Begin Creating New Graphs

xy = np.vstack([data['LivingArea'], data['Price']])
z = gaussian_kde(xy)(xy)

# Adding transparency to Scatter plot for Price aand Area 
plt.figure(figsize=(12, 8))
plt.scatter(data['LivingArea'], data['Price'], alpha=0.2) 
plt.title('Price vs. Living Area')
plt.xlabel('Living Area (sqft)')
plt.ylabel('Price')
plt.tight_layout()
plt.savefig(f'{image_path}\\Price_Area.png')

# Adding Transperency to Price and Distance 
plt.figure(figsize=(12, 8))
plt.scatter(data['Distance to the university (in miles)'], data['Price'], alpha=0.1)  # Adjust alpha as needed
plt.title('Price vs. Distance to the University')
plt.xlabel('Distance to UT Austin (miles)')
plt.ylabel('Price')
plt.tight_layout()
plt.savefig(f'{image_path}\\Price_Distance.png')

# Adding Transperency to Price and ZipCode 
plt.figure(figsize=(10, 6))
plt.scatter(data['Zip'], data['Price'], alpha=0.6, edgecolors='none', s=30, cmap='viridis')
plt.title('Zip_Code vs. Price')
plt.xlabel('Zip Code')
plt.ylabel('Price')
plt.tight_layout()
plt.savefig(f'{image_path}\\Price_Zip.png')