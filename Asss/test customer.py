import pandas as pd
import matplotlib.pyplot as plt

# Load the data
file_path = "C:\\Users\\Acer\\Downloads\\Asss\\Customer.csv"
data = pd.read_csv(file_path)

# Group by country and count the occurrences
country_counts = data['Country'].value_counts()

# Plotting the pie chart
plt.figure(figsize=(8, 8))
plt.pie(country_counts, labels=country_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title("Distribution of Countries Based on Customer Purchases")
plt.show()
