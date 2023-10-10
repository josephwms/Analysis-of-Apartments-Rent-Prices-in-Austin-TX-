import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, explained_variance_score, mean_absolute_error

# Load your CSV file
data = pd.read_csv('artifacts/result.csv')

# Use the selected columns as X
X = data.iloc[:, [1, 3, 5, 6, 7]]

# Use the first column (price) as Y
y = data.iloc[:, 0]

# split data into training and testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Initialize the Random Forest regressor
rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model on the training data
rf_regressor.fit(X_train, y_train)

# Make predictions on the test data
y_pred = rf_regressor.predict(X_test)


''''Evaluate the model, we don't have to print all the evaluation metrics, 
just pick out those metrics that can clearly show the performance and easy to be interpreted.'''

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
explained_variance = explained_variance_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f"R-squared (R2) Score: {r2}")

Y_pred = rf_regressor.predict(X)
data['pred_price'] = Y_pred
data.to_csv('artifacts/result_with_predict.csv', index=False)

'''Interaction with users'''

zip_code = str(input("Please input the expected zip code (in Austin, TX) of your apartment: ")) # input an integer like 78712, 78750, etc.
distance = str(input("Please input the expected distance (in miles and keep two decimal places) to UT Austin of your apartment: ")) # input a float like 0.85, 1.56, 2.08, etc.
bathrooms = str(input("Please input the expected number of bathrooms of your apartment: ")) # input an integer like 1, 2, 3, etc.
bedrooms = str(input("Please input the expected number of bedrooms of your apartment: ")) # input an integer like 1, 2, 3, etc.
living_area = str(input("Please input the expected living area in sqft. of your apartment: ")) # input a float like 1020, 805, 1874, etc.

data_user = {
    'Zip': zip_code,
    'Distance to the university (in miles)': distance,
    'Bathrooms': bathrooms,
    'Bedrooms': bedrooms,
    'LivingArea': living_area
}

X_user = pd.DataFrame(data_user, index=[0])

Y_user = rf_regressor.predict(X_user)

print(f'The estimated cost for your expected apartment is: {Y_user[0]}')







