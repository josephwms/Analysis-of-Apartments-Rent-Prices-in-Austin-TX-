import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, explained_variance_score, mean_absolute_error
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load your CSV file
data = pd.read_csv('artifacts/result.csv')


# Use the selected columns as X
X = data.iloc[:, [1, 3, 5, 6, 7]]
# Use the first column (price) as Y
y = data.iloc[:, 0]

# split data into training and testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize X
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
X_scaled = scaler.transform(X)

# Initialize the Random Forest regressor
dt_regressor = DecisionTreeRegressor(random_state=42)

# Train the model on the training data
dt_regressor.fit(X_train_scaled, y_train)

# Make predictions on the test data
y_pred = dt_regressor.predict(X_test_scaled)


''''Evaluate the model, we don't have to print all the evaluation metrics, 
just pick out those metrics that can clearly show the performance and easy to be interpreted.'''

# evaluate the model
# calculate the middle products
n = X_test_scaled.shape[0] # number of observations
p = X_test_scaled.shape[1] # number of coefficients except intercept
residuals = y_test - dt_regressor.predict(X_test_scaled)
rss = np.sum(residuals ** 2)

# calculate the final results
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
explained_variance = explained_variance_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
adjusted_r_squared = 1 - (1 - r2) * ((n - 1) / (n - p - 1))
aic = 2 * p + n * np.log(rss / n)
bic = n * np.log(rss / n) + (p+1) * np.log(n)

# show the result
print(f"R-squared (R2) Score: {r2}")
print(f"Adjusted R-squared: {adjusted_r_squared}")
print(f"Mean Squared Error: {mse}")
print(f"Mean Absolute Error: {mae}")
print(f"AIC: {aic}")
print(f"BIC: {bic}")

