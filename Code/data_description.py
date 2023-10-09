import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read the csv file and change the distance variable into
data = pd.read_csv('artifacts/result.csv')
data.iloc[:, 3] = data.iloc[:, 3].str[:4]

# Use the selected columns as X
X = data.iloc[:, [1, 3, 5, 6, 7]]
# Use the first column (price) as Y
Y = data.iloc[:, 0]

# Part 1: the brief overview of the data

# price
print(Y.describe())
plt.hist(data.iloc[:,0])
plt.title('Histogram of price')
plt.show()

# zipcode
print(data.iloc[:,1].describe())
plt.hist(data.iloc[:,1])
plt.title('Histogram of Zipcode')
plt.show()

# Distance to the university
print(data.iloc[:,3].describe())
plt.hist(data.iloc[:,3],bins=30)
plt.title('Histogram of Distance to the university')
plt.show()

# Bathrooms
print(data.iloc[:,5].describe())
plt.hist(data.iloc[:,5])
plt.title('Histogram of Bathrooms')
plt.show()

# Bedrooms
print(data.iloc[:,6].describe())
plt.hist(data.iloc[:,6])
plt.title('Histogram of Bedrooms')
plt.show()

# Living area
print(data.iloc[:,7].describe())
plt.hist(data.iloc[:,7])
plt.title('Histogram of Living Area')
plt.show()

# Part 2: the relationship between X and Y

corr_matrix = data.iloc[:,[0,1,3,5,6,7]].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix Heatmap')
plt.show()
# We can see bathrooms and living area has stronger correlation with price.
# Surprisingly, the distance to school seems weakly correlated to price.
# Let see how the data maps with graph.

# Price & zipcode
plt.scatter(X.iloc[:,0],Y)
plt.xlabel('Zipcode')
plt.ylabel('Price')
plt.title('Scatter plot of Price and Zipcode')
plt.show()

# Price & Distance
plt.scatter(X.iloc[:,1],Y)
plt.xlabel('Distance')
plt.ylabel('Price')
plt.title('Scatter plot of Price and Distance to the University')
plt.show()

# Price & Bathrooms
plt.scatter(X.iloc[:,2],Y)
plt.xlabel('Bathrooms')
plt.ylabel('Price')
plt.title('Scatter plot of Price and Bathrooms')
plt.show()

# Price & Bedrooms
plt.scatter(X.iloc[:,3],Y)
plt.xlabel('Bedrooms')
plt.ylabel('Price')
plt.title('Scatter plot of Price and Bedrooms')
plt.show()

# Price & Living Area
plt.scatter(X.iloc[:,4],Y)
plt.xlabel('Living Area')
plt.ylabel('Price')
plt.title('Scatter plot of Price and Living Area')
plt.show()



