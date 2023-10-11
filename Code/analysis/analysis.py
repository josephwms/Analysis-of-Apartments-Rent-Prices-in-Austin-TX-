import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import os
print(os.getcwd())

df = pd.read_csv('../../artifacts/result.csv')

print(df.head())
print(df.info())
print(df.describe())

sns.scatterplot(x='Bedrooms', y='Price', data=df)
plt.xlabel('Number of Rooms')
plt.ylabel('Rent Price ($)')
plt.title('Impact of Number of # of Rooms on Rent')
plt.xticks(range(1, 5)) 
plt.show()

correlation = df['Bedrooms'].corr(df['Price'])
print(f"Correlation between Number of Rooms and Rent Price: {correlation}")

'''We see a moderate positive linear relationship between two variables: Price and # of bedrooms. As # of bedrooms increase so does price moderately.'''

'''Lets see what is the average rent for different number of rooms'''
average_rent_by_rooms = df.groupby('Bedrooms')['Price'].mean()

plt.figure(figsize=(8, 6))
average_rent_by_rooms.plot(kind='bar', color='blue')
plt.title('Average Rent by Number of Rooms')
plt.xlabel('Number of Rooms')
plt.ylabel('Average Rent ($)')
plt.xticks(rotation=0)  
plt.grid(axis='y')
plt.show()

'''Now lets check the impact on price from the distance to university'''

plt.scatter(df['Distance to the university (in miles)'], df['Price'])
plt.xlabel('Distance to the university (in miles)')
plt.ylabel('Rental Rate')
plt.title('Scatterplot of Distance vs. Rental Rate')
plt.show()

'''There doesnt seem much of a pattern in distance vs rent'''

'''Analyze how much variance in the rental rates is explained by distance from the university'''

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

X = df['Distance to the university (in miles)']
y = df['Price']
X = X.values.reshape(-1, 1)

model = LinearRegression()
model.fit(X,y)


print(f'Intercept: {model.intercept_}')
print(f'Coefficient for Distance to the university: {model.coef_[0]}')

y_predict = model.predict(X)

plt.scatter(X, y, label='Data')
plt.plot(X, y_predict, color='red', label='Regression Line')
plt.xlabel('Distance from University')
plt.ylabel('Rental Rate')
plt.title('Linear Regression: Distance vs. Rental Rate')
plt.legend()
plt.show()


r2 = r2_score(y, y_predict)
print(f'R-squared for distance: {r2}')

'''The coefficient is positive but small and the intercept is a big value. The relationship is positive but very little variance in rent is explained by distance from the unversity alone which means there are other factors playing a role. '''

'''Lets see the effect of taking both distance from university and number of bedrooms into account. '''

X1 = df[['Distance to the university (in miles)', 'Bedrooms']]
y1 = df['Price']

model = LinearRegression()
model.fit(X1, y1)

print(f'Intercept: {model.intercept_}')
print(f'Coefficient for Distance to the university: {model.coef_[0]}')
print(f'Coefficient for Bedrooms: {model.coef_[1]}')

y_pred = model.predict(X1)

r2_ = r2_score(y1, y_pred)

print(f'R-squared for distance and bedrooms: {r2_}')

'''Now taking both the variables into account gives a relatively bigger r2 which means a lot more variance in rent is explained when these two factors/variables are accounted for together. The relationship is negative with distance and positive with number of bedrooms as expected.'''

'''Lets see which zipcodes have the highest rents'''

zipcode_rents = df.groupby('Zip')['Price'].mean().reset_index()

zipcode_rents = zipcode_rents.sort_values(by='Price', ascending=False)

top_n = 10
top_zipcodes = zipcode_rents['Zip'][:top_n].astype(str)
top_rents = zipcode_rents['Price'][:top_n]

plt.figure(figsize=(12, 6))
plt.bar(top_zipcodes, top_rents)
plt.xlabel('Zip Code')
plt.ylabel('Average Price')
plt.title(f'Top {top_n} Most Expensive Zip Codes')
plt.xticks(top_zipcodes, rotation=45)
plt.show()

'''I think it would also be interesting to see the impact of area on rents'''

X2 = df['LivingArea'].values.reshape(-1, 1)
y2 = df['Price'].values

model = LinearRegression()
model.fit(X2,y2)

print(f'Intercept: {model.intercept_}')
print(f'Coefficient for living area: {model.coef_[0]}')

y_predicted = model.predict(X2)

plt.figure(figsize=(10, 6))
plt.scatter(X2, y2, label='Original Data')
plt.plot(X2, y_predicted, color='red', linewidth=2, label='Linear Regression')
plt.xlabel('Living Area (sq. ft)')
plt.ylabel('Rent')
plt.title('Impact of Living Area on Rent')
plt.legend()
plt.grid(True)
plt.show()

r2__ = r2_score(y2, y_predicted)
print(f'R-squared for living area: {r2__}')

'''Calculate the correlation matrix'''
correlation_matrix = df[['LivingArea', 'Price']].corr()

'''Extract the correlation coefficient between LivingArea and Rent'''
correlation_coefficient = correlation_matrix.loc['LivingArea', 'Price']

print(f"Correlation Coefficient: {correlation_coefficient}")

'''There is a moderately strong positive relationship between living area and rent which means as living area increases then so does rent. Also, about 50% variability in rent is explained by living area'''

# Please Set the base path for images. Here is mine as an example
image_path = '../../images'

# Extract the relevant columns
price = df["Price"]
living_area = df["LivingArea"]
distance = df["Distance to the university (in miles)"]
bathroom = df["Bathrooms"]
bedroom = df["Bedrooms"]
zip_code = df["Zip"]

# Set the style and context for the plot
sns.set(style="whitegrid")
sns.set_context("talk")

# Creating Box Plot for Price and Distance
bins_distance = [0, 1, 2, 3, 6, 11, 20]
labels_distance = ["0-1", "1-2", "2-3", "3-6", "6-11", "11-20"]
df["Binned_Distance"] = pd.cut(
    df["Distance to the university (in miles)"],
    bins=bins_distance,
    labels=labels_distance,
    right=False,
)

# Get default palette color
default_color = sns.color_palette()[0]

# Define properties for box and outlier
boxprops = {"facecolor": default_color, "color": default_color}
flierprops = {
    "markerfacecolor": default_color,
    "markeredgecolor": default_color,
    "markersize": 5,
}

plt.figure(figsize=(12, 8))
sns.boxplot(
    x="Binned_Distance",
    y="Price",
    data=df,
    boxprops=boxprops,
    flierprops=flierprops,
    color=default_color,
)
plt.title("Price vs. Binned Distance to the University")
plt.xlabel("Binned Distance to UT Austin (miles)")
plt.ylabel("Price")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{image_path}\\Price_Distance_Box.png")

# Creting a box plot that only graphs specific zip codes

min_listings = 50
zip_counts = df["Zip"].value_counts()
zip_to_include = zip_counts[zip_counts > min_listings].index

filtered_data = df[df["Zip"].isin(zip_to_include)]

# Box Plot for Price and Filtered Zip Codes

# Get default palette color
default_color = sns.color_palette()[0]

# Define properties for box and outlier
boxprops_zip = {"facecolor": default_color, "color": default_color}
flierprops_zip = {
    "markerfacecolor": default_color,
    "markeredgecolor": default_color,
    "markersize": 5,
}

plt.figure(figsize=(15, 8))
sns.boxplot(
    x="Zip",
    y="Price",
    data=filtered_data,
    boxprops=boxprops_zip,
    flierprops=flierprops_zip,
    color=default_color,
)
plt.title("Price vs. Zip Code (with at least {} listings)".format(min_listings))
plt.xlabel("Zip Code")
plt.ylabel("Price")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{image_path}\\Price_Zip_Box.png")