import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('artifacts/result.csv')

print(df.head())
print(df.info())
print(df.describe())

sns.scatterplot(x='Bedrooms', y='Price', data=df)
plt.xlabel('Number of Rooms')
plt.ylabel('Rent Price ($)')
plt.title('Impact of Number of # of Rooms on Rent')
plt.show()

correlation = df['Bedrooms'].corr(df['Price'])
print(f"Correlation between Number of Rooms and Rent Price: {correlation}")

#We see a moderate positive linear relationship between two variables: Price and # of bedrooms. As # of bedrooms increase so does price moderately.