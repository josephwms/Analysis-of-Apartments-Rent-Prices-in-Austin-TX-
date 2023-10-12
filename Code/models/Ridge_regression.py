import pandas as pd
from sklearn import linear_model
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, explained_variance_score, mean_absolute_error
from sklearn.preprocessing import StandardScaler

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

# Choose the regularization parameter
reg = linear_model.RidgeCV(alphas=np.logspace(-6, 6, 13))
reg.fit(X_train_scaled, Y_train)
ridge_alpha = reg.alpha_

# run the result ridge regression
model = linear_model.Ridge(alpha=ridge_alpha)
model.fit(X_train_scaled, Y_train)
Y_pred = model.predict(X_test_scaled)

# evaluate the model
# calculate the middle products
n = X_test_scaled.shape[0]  # number of observations
p = X_test_scaled.shape[1]  # number of coefficients except intercept
residuals = Y_test - model.predict(X_test_scaled)
rss = np.sum(residuals**2)
sum_percentage_error = 0

# calculate the final results
mse = mean_squared_error(Y_test, Y_pred)
r2 = r2_score(Y_test, Y_pred)
explained_variance = explained_variance_score(Y_test, Y_pred)
mae = mean_absolute_error(Y_test, Y_pred)
adjusted_r_squared = 1 - (1 - r2) * ((n - 1) / (n - p - 1))
aic = 2 * p + n * np.log(rss / n)
bic = n * np.log(rss / n) + (p + 1) * np.log(n)
rmse = mse**(1/2)
for i in range(n):
    if Y_test.iloc[i] != 0:  # Avoid division by zero
        percentage_error = ((Y_test.iloc[i] - Y_pred[i]) / Y_test.iloc[i]) * 100
        sum_percentage_error += percentage_error
mpe = sum_percentage_error / n

# show the result
print(f'R-squared (R2) Score: {r2}')
print(f'Adjusted R-squared: {adjusted_r_squared}')
print(f'Mean Squared Error: {mse}')
print(f'Mean Absolute Error: {mae}')
print(f'AIC: {aic}')
print(f'BIC: {bic}')
print(f'Rooted Mean Squared Error: {rmse}')
print(f'Mean Percentage Error: {mpe}')
