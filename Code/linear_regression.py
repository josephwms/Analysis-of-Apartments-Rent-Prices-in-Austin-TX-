import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import os

print(os.getcwd())
# Load your CSV file
data = pd.read_csv('artifacts/result.csv')

# Use the selected columns as X, including the new interaction and squared terms
X = data[['Zip', 'Distance to the university (in miles)', 'Bathrooms', 'Bedrooms', 'LivingArea']]
y = data['Price']  # Target variable remains the same

# Split data into training and testing set
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Linear Regression model
lr_regressor = LinearRegression().fit(x_train, y_train)

# Make predictions on the test data
y_pred = lr_regressor.predict(x_test)

# Evaluate the model
r2 = r2_score(y_test, y_pred)
print(f"R-squared (R2) Score: {r2}")

# Predict on the entire dataset
Y_pred = lr_regressor.predict(X)
data['pred_rent'] = Y_pred
data.to_csv(r'C:\Users\aahil\Documents\repos\eco395m-project1-midterm\artifacts\result_with_LR_predict.csv', index=False)