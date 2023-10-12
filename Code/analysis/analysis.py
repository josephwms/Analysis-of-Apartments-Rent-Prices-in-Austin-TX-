import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings

warnings.simplefilter('ignore')

df = pd.read_csv('artifacts/result.csv')

image_path = 'images/'

'''Description of data'''

print('Head')
print(df.head())
print('-------------------------------------------------------------')
print('Info')
print(df.info())
print('-------------------------------------------------------------')
print('Description')
print(df.describe())
print('-------------------------------------------------------------')

'''Histogram of rent'''
plt.figure(figsize=(10, 6))
plt.hist(df['Price'], bins=10, color='blue', edgecolor='black')
plt.xlabel('Rent Amount')
plt.ylabel('Frequency')
plt.title('Rent Distribution Histogram')
plt.savefig(f'{image_path}/Rent_Distribution.png')

'''Impact of number of bedrooms on rent'''
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Bedrooms', y='Price', data=df)
plt.xlabel('Number of Rooms')
plt.ylabel('Rent Price ($)')
plt.title('Impact of # of Rooms on Rent')
plt.xticks(range(1, 5))
plt.savefig(f'{image_path}/Impact_of_Rooms_numbers_on_Rent.png')


correlation = df['Bedrooms'].corr(df['Price'])
print(f'Correlation between Number of Rooms and Rent Price: {correlation}')
print('-------------------------------------------------------------')

'''Average rent based on number of bedrooms'''
average_rent_by_rooms = df.groupby('Bedrooms')['Price'].mean()

plt.figure(figsize=(10, 6))
average_rent_by_rooms.plot(kind='bar', color='blue')
plt.title('Average Rent by Number of Rooms')
plt.xlabel('Number of Rooms')
plt.ylabel('Average Rent ($)')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.savefig(f'{image_path}/Average_Rent_by_Number_of_Rooms.png')

'''Impact of distance from university on rent'''
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df,
                x='Distance to the university (in miles)',
                y='Price',
                hue='Bedrooms',
                palette='viridis')
plt.xlabel('Distance to the university (in miles)')
plt.ylabel('Rental Rate')
plt.title('Scatterplot of Distance vs. Rental Rate')
plt.legend(title=' # of Bedrooms')
plt.savefig(f'{image_path}/Scatterplot_Distance_vs._Rental_Rates.png')

'''There doesnt seem much of a pattern in distance vs rent'''

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

X = df['Distance to the university (in miles)']
y = df['Price']
X = X.values.reshape(-1, 1)

model = LinearRegression()
model.fit(X, y)

print(f'Intercept: {model.intercept_}')
print(f'Coefficient for Distance to the university: {model.coef_[0]}')
print('-------------------------------------------------------------')
y_predict = model.predict(X)

plt.figure(figsize=(10, 6))
plt.scatter(X, y, label='Data')
plt.plot(X, y_predict, color='red', label='Regression Line')
plt.xlabel('Distance from University')
plt.ylabel('Rental Rate')
plt.title('Linear Regression: Distance vs. Rental Rate')
plt.legend()
plt.savefig(f'{image_path}/Linear_Regression_Distance_vs._Rental_Rate.png')


r2 = r2_score(y, y_predict)
print(f'R-squared for distance: {r2}')
print('-------------------------------------------------------------')
'''The coefficient is positive but small and the intercept is a big value. The relationship is positive but very little variance in rent is explained by distance from the unversity alone which means there are other factors playing a role. '''
'''Lets see the effect of taking both distance from university and number of bedrooms into account. '''

X1 = df[['Distance to the university (in miles)', 'Bedrooms']]
y1 = df['Price']

model = LinearRegression()
model.fit(X1, y1)

print(f'Intercept: {model.intercept_}')
print(f'Coefficient for Distance to the university: {model.coef_[0]}')
print(f'Coefficient for Bedrooms: {model.coef_[1]}')
print('-------------------------------------------------------------')
y_pred = model.predict(X1)

r2_ = r2_score(y1, y_pred)

print(f'R-squared for distance and bedrooms: {r2_}')
print('-------------------------------------------------------------')
'''Now taking both the variables into account gives a relatively bigger r2 which means a lot more variance in rent is explained when these two factors/variables are accounted for together. The relationship is negative with distance and positive with number of bedrooms as expected.'''

'''Top most expensive zipcodes'''
zipcode_rents = df.groupby('Zip')['Price'].mean().reset_index()

zipcode_rents = zipcode_rents.sort_values(by='Price', ascending=False)

top_n = 10
top_zipcodes = zipcode_rents['Zip'][:top_n].astype(str)
top_rents = zipcode_rents['Price'][:top_n]

plt.figure(figsize=(10, 6))
plt.bar(top_zipcodes, top_rents)
plt.xlabel('Zip Code')
plt.ylabel('Average Price')
plt.title(f'Top {top_n} Most Expensive Zip Codes')
plt.xticks(top_zipcodes, rotation=45)
plt.savefig(f'{image_path}/Top_{top_n}_Most_Expensive_Zip_Codes.png')

'''Impact of living area on rent'''
X2 = df['LivingArea'].values.reshape(-1, 1)
y2 = df['Price'].values

model = LinearRegression()
model.fit(X2, y2)

print(f'Intercept: {model.intercept_}')
print(f'Coefficient for living area: {model.coef_[0]}')
print('-------------------------------------------------------------')
y_predicted = model.predict(X2)

plt.figure(figsize=(10, 6))
plt.scatter(X2, y2, label='Original Data')
plt.plot(X2, y_predicted, color='red', linewidth=2, label='Linear Regression')
plt.xlabel('Living Area (sq. ft)')
plt.ylabel('Rent')
plt.title('Impact of Living Area on Rent')
plt.legend()
plt.savefig(f'{image_path}/Impact_of_Living_Area_on_Rent.png')


r2__ = r2_score(y2, y_predicted)
print(f'R-squared for living area: {r2__}')
print('-------------------------------------------------------------')

correlation_matrix = df[['LivingArea', 'Price']].corr()

correlation_coefficient = correlation_matrix.loc['LivingArea', 'Price']

print(f'Correlation Coefficient: {correlation_coefficient}')
print('-------------------------------------------------------------')

'''Graphing box plots'''
price = df['Price']
living_area = df['LivingArea']
distance = df['Distance to the university (in miles)']
bathroom = df['Bathrooms']
bedroom = df['Bedrooms']
zip_code = df['Zip']

sns.set(style='whitegrid')
sns.set_context('talk')

bins_distance = [0, 1, 2, 3, 6, 11, 20]
labels_distance = ['0-1', '1-2', '2-3', '3-6', '6-11', '11-20']
df['Binned_Distance'] = pd.cut(
    df['Distance to the university (in miles)'],
    bins=bins_distance,
    labels=labels_distance,
    right=False,
)


default_color = sns.color_palette()[0]


boxprops = {'facecolor': default_color, 'color': default_color}
flierprops = {
    'markerfacecolor': default_color,
    'markeredgecolor': default_color,
    'markersize': 5,
}

plt.figure(figsize=(10, 6))
sns.boxplot(
    x='Binned_Distance',
    y='Price',
    data=df,
    boxprops=boxprops,
    flierprops=flierprops,
    color=default_color,
)
plt.title('Price vs. Binned Distance to the University')
plt.xlabel('Binned Distance to UT Austin (miles)')
plt.ylabel('Price')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f'{image_path}/Price_Distance_Box.png')

min_listings = 50
zip_counts = df['Zip'].value_counts()
zip_to_include = zip_counts[zip_counts > min_listings].index

filtered_data = df[df['Zip'].isin(zip_to_include)]

default_color = sns.color_palette()[0]

boxprops_zip = {'facecolor': default_color, 'color': default_color}
flierprops_zip = {
    'markerfacecolor': default_color,
    'markeredgecolor': default_color,
    'markersize': 5,
}

plt.figure(figsize=(10, 6))
sns.boxplot(
    x='Zip',
    y='Price',
    data=filtered_data,
    boxprops=boxprops_zip,
    flierprops=flierprops_zip,
    color=default_color,
)
plt.title(
    'Price vs. Zip Code (with at least {} listings)'.format(min_listings))
plt.xlabel('Zip Code')
plt.ylabel('Price')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f'{image_path}/Price_Zip_Box.png')

'''Summary statistics'''
summary_distance = df.groupby('Binned_Distance')['Price'].describe()

print('Summary Statistics for Price based on Binned Distance to the University:')
print(summary_distance)

summary_zip = filtered_data.groupby('Zip')['Price'].describe()

print('\nSummary Statistics for Price based on Zip Code (with at least {} listings):'.format(min_listings))
print(summary_zip)

'''Trend lines'''
df.iloc[:, 3] = sorted(df.iloc[:, 3])

sns.set(style='whitegrid')
sns.set_context('talk')

plt.figure(figsize=(10, 6))
sns.lineplot(x=living_area, y=price, marker='o', color='b', linewidth=2)
plt.title('Living Area vs. Price')
plt.xlabel('Living Area')
plt.ylabel('Price')

plt.savefig('images/Price_Area.png')

plt.figure(figsize=(10, 6))
sns.lineplot(x=bathroom, y=price, marker='o', color='b', linewidth=2)
plt.title('Bathroom vs. Price')
plt.xticks(range(1, 5))
plt.xlabel('Bathrooms')
plt.ylabel('Price')
plt.savefig('images/Price_Bathrooms.png')

plt.figure(figsize=(10, 6))
sns.lineplot(x=bedroom, y=price, marker='o', color='b', linewidth=2)
plt.title('Bedroom vs. Price')
plt.xticks(range(1, 5))
plt.xlabel('Bedrooms')
plt.ylabel('Price')
plt.savefig('images/Price_Bedrooms.png')

plt.figure(figsize=(10, 6))
sns.lineplot(x=zip_code, y=price, marker='o', color='b', linewidth=2)
plt.title('Zip_Code vs. Price')
plt.xlabel('Zip Code')
plt.ylabel('Price')
plt.savefig('images/Price_Zip.png')

print('All figures are saved in the images folder')
