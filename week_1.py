#client Project :- Create a basic data processing script

# Average Temperature Calculator

days = int(input("Enter number of days: "))

total_temperature = 0

for i in range(days):
    temp = float(input(f"Enter temperature for day {i+1}: "))
    total_temperature += temp

average = total_temperature / days

print("Average Temperature is:", average)
