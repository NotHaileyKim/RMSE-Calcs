import math
import numpy as np
import pandas as pd

# Replace 'path_to_the_file.csv' with the path to your actual CSV file
csv_file_path = 'path_to_the_file.csv'

# Load your CSV file
data = pd.read_csv(csv_file_path)

# Assuming your CSV has columns named 'Actual' and 'Predicted'
y_actual = data['Actual'].values
y_predicted = data['Predicted'].values

# Calculate MSE
MSE = np.square(np.subtract(y_actual, y_predicted)).mean()

# Calculate RMSE
RMSE = math.sqrt(MSE)

print("Root Mean Square Error:\n", RMSE)