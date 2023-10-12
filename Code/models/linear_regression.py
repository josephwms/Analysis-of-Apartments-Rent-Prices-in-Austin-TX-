import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error, explained_variance_score
import os
import numpy as np
from sklearn.preprocessing import StandardScaler

print(os.getcwd())
# Load your CSV file
data = pd.read_csv('artifacts/result.csv')

# Use the selected columns as X, including the new interaction and squared terms
X = data[[
    'Zip', 'Distance to the university (in miles)', 'Bathrooms', 'Bedrooms',
    'LivingArea'
]]
y = data['Price']  # Target variable remains the same

# Split data into training and testing set
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.2,
                                                    random_state=42)

# Standardize X
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
X_scaled = scaler.transform(X)

# Initialize and train the Linear Regression model
lr_regressor = LinearRegression().fit(X_train_scaled, y_train)

# Make predictions on the test data
y_pred = lr_regressor.predict(X_test_scaled)

# evaluate the model
# calculate the middle products
n = X_test.shape[0]  # number of observations
p = X_test.shape[1]  # number of coefficients except intercept
residuals = y_test - lr_regressor.predict(X_test)
rss = np.sum(residuals**2)

# calculate the final results
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
explained_variance = explained_variance_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
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
