import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score, explained_variance_score, mean_absolute_error
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
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

# Choose the regularization parameter
model_test = SVR(kernel='rbf')
param_grid = {'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000]}
grid_search = GridSearchCV(model_test,
                           param_grid,
                           cv=5,
                           scoring='neg_mean_squared_error')
grid_search.fit(X_train_scaled, Y_train)
best_C = grid_search.best_params_['C']

# run the result support vector machines regression
model = SVR(kernel='rbf', C=best_C)
model.fit(X_train_scaled, Y_train)
Y_pred = model.predict(X_test_scaled)

# evaluate the model
# calculate the middle products
n = X_test_scaled.shape[0]  # number of observations
p = X_test_scaled.shape[1]  # number of coefficients except intercept
residuals = Y_test - model.predict(X_test_scaled)
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
