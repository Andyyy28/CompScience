#Linear Regression
import numpy as np
import matplotlib.pyplot as plt

# Sample data on predicting how long it takes to travel based on the distance covered.
distance = np.array([5.1, 12.7, 18.5, 21.3, 28.9, 30.2])  # Independent variable (x)
travel_time = np.array([10.2, 21.5, 29.1, 36.2, 43.0, 56.3])  # Dependent variable (y)

# Step 1: Calculate means of x and y
x_mean = np.mean(distance)
y_mean = np.mean(travel_time)

# Step 2: Calculate slope (m)
numerator = np.sum((distance - x_mean) * (travel_time - y_mean))  # Covariance of x and y
denominator = np.sum((distance - x_mean) ** 2)  # Variance of x
slope = numerator / denominator

# Step 3: Calculate intercept (b)
intercept = y_mean - slope * x_mean

# Step 4: Use the regression equation to predict y values
predicted_time = slope * distance + intercept

# Output the results
print("Linear Regression Results:")
print(f"Mean of Distance (x): {x_mean}")
print(f"Mean of Predicted Travel Time (y): {y_mean}")
print(f"Slope (m): {slope}")
print(f"Intercept (b): {intercept}")
print("Regression Equation: y = {:.2f}x + {:.2f}".format(slope, intercept))

# Step 5: Plot the results
plt.figure(figsize=(8, 5))
plt.scatter(distance, travel_time, color='blue', label='Actual Data')
plt.plot(distance, predicted_time, color='red', label=f'Regression Line (y = {slope:.2f}x + {intercept:.2f})')
plt.title('Linear Regression: Distance vs Travel Time')
plt.xlabel('Distance (km)')
plt.ylabel('Travel Time (minutes)')
plt.legend()
plt.grid(True)
plt.show()
