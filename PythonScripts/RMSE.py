import math
import numpy as np
import pandas as pd

import csv

# Data to be written to the CSV file
data = [
    ["name", "age", "city"],
    ["John", "30", "New York"],
    ["Jane", "25", "Los Angeles"]
]

# Open a new CSV file for writing
with open('mydata.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the data to the CSV file
    writer.writerows(data)

print("CSV file has been created successfully.")
# Replace 'path_to_the_file.csv' with the path to  actual CSV file
csv_file_path = 'path_to_the_file.csv'


# Load  CSV file
data = pd.read_csv(csv_file_path)

# Assuming  CSV has columns named 'Actual' and 'Predicted'
y_actual = data['Actual'].values
y_predicted = data['Predicted'].values


# Calculate MSE
MSE = np.square(np.subtract(y_actual, y_predicted)).mean()

# Calculate RMSE
RMSE = math.sqrt(MSE)

print("Root Mean Square Error:\n", RMSE)
