import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, explained_variance_score, mean_absolute_error
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
import numpy as np

# read the csv file
data = pd.read_csv('artifacts/result.csv')

# Use the selected columns as X
X = data.iloc[:, [1, 3, 5, 6, 7]]
# Use the first column (price) as Y
Y = data.iloc[:, 0]

# split data into training and testing set
X_train, X_test, Y_train, Y_test = train_test_split(X,
                                                    Y,
                                                    test_size=0.2,
                                                    random_state=42)

# Standardize X
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
X_scaled = scaler.transform(X)

# run the result 3rd degree polynomial regression
poly_features = PolynomialFeatures(degree=3)
X_poly_train = poly_features.fit_transform(X_train_scaled)
X_poly_test = poly_features.fit_transform(X_test_scaled)
model = LinearRegression()
model.fit(X_poly_train, Y_train)
Y_pred = model.predict(X_poly_test)

# evaluate the model
# calculate the middle products
n = X_poly_test.shape[0]  # numbers of observations
p = X_poly_test.shape[1]  # number of coefficients except intercept
residuals = Y_test - model.predict(X_poly_test)
rss = np.sum(residuals**2)

# calculate the final results
mse = mean_squared_error(Y_test, Y_pred)
r2 = r2_score(Y_test, Y_pred)
explained_variance = explained_variance_score(Y_test, Y_pred)
mae = mean_absolute_error(Y_test, Y_pred)
adjusted_r_squared = 1 - (1 - r2) * ((n - 1) / (n - p - 1))
aic = 2 * p + n * np.log(rss / n)
bic = n * np.log(rss / n) + (p + 1) * np.log(n)

# show the result
print(f'R-squared (R2) Score: {r2}')
print(f'Adjusted R-squared: {adjusted_r_squared}')
print(f'Mean Squared Error: {mse}')
print(f'Mean Absolute Error: {mae}')
print(f'AIC: {aic}')
print(f'BIC: {bic}')
