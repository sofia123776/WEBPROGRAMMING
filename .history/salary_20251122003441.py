# Importing necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd

# Sample dataset
data = {
    "Experience (Years)": [1, 2, 3, 4, 5],
    "Salary (K)": [40, 50, 60, 70, 80]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Features (X) and Target (y)
X = df[["Experience (Years)"]]
y = df["Salary (K)"]

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate Mean Squared Error
mse = mean_squared_error(y_test, y_pred)

# Display results
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("Mean Squared Error:", mse)

# Example prediction
experience = np.array([[6]])  # Predict salary for 6 years of experience
predicted_salary = model.predict(experience)
print(f"Predicted salary for 6 years of experience: {predicted_salary[0]}K")
