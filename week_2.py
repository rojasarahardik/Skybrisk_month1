# Data Cleaning Project

user_input = input("Enter numbers separated by spaces: ")

# Convert input into list
data = list(map(int, user_input.split()))

unique_data = []
duplicates = []

# Remove duplicates
for num in data:
    if num not in unique_data:
        unique_data.append(num)
    else:
        duplicates.append(num)

threshold = int(input("Enter threshold value: "))

# Filter data
filtered_data = [x for x in unique_data if x > threshold]

print("\nOriginal Data:", data)
print("Duplicate Values Removed:", duplicates)
print("Cleaned Data:", unique_data)
print("Filtered Data:", filtered_data)