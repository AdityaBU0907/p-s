import random

# Function to calculate the mean of a dataset
def calculate_mean(data):
    return sum(data) / len(data)

# Function to calculate the covariance between two datasets
def calculate_covariance(x_data, y_data):
    mean_x = calculate_mean(x_data)
    mean_y = calculate_mean(y_data)
    
    covariance = sum((x - mean_x) * (y - mean_y) for x, y in zip(x_data, y_data)) / (len(x_data) - 1)
    
    return covariance

# Generate two random lists of integers between 1 and 100
x_data = [random.randint(1, 100) for _ in range(100)]
y_data = [random.randint(1, 100) for _ in range(100)]

# Calculate and print covariance
covariance = calculate_covariance(x_data, y_data)
print(f"Covariance: {covariance}")
