import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load the datase
file_path = r"C:\Users\Acer\Downloads\Asss\WebsiteAccessCategory.csv"
data = pd.read_csv(file_path)

# Preprocess the data
data['AccessDate'] = pd.to_datetime(data['AccessDate'])
data['AccessYear'] = data['AccessDate'].dt.year
data['AccessMonth'] = data['AccessDate'].dt.month

# Selecting relevant features for prediction
# We assume that 'TimeSpent' can be predicted based on other features.
X = data[['AccessYear', 'AccessMonth', 'DeviceUsed', 'CategoryViewed', 'BrowserUsed']]
y = data['TimeSpent']

# Convert categorical data to numerical
X = pd.get_dummies(X, drop_first=True)

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict the future growth based on the test set
y_pred = model.predict(X_test)

# Calculate the error
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Plotting the results
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color='blue')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', lw=2)
plt.xlabel('Actual Time Spent')
plt.ylabel('Predicted Time Spent')
plt.title('Actual vs Predicted Time Spent')
plt.show()
