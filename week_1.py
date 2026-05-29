
#client Project :- Create a basic data processing script

# Average Temperature Calculator

days = int(input("Enter number of days: "))

total_temperature = 0

for i in range(days):
    temp = float(input(f"Enter temperature for day {i+1}: "))
    total_temperature += temp

average = total_temperature / days

print("Average Temperature is:", average)


"""
summary :-

In Week 1, I learned the fundamentals of Python programming. 
I studied variables, data types, operators, input/output statements, conditional statements (if-else), and loops (for and while).
I created basic Python programs such as:
Temperature Converter
Simple Calculator
I also worked on a basic data processing project to calculate the average temperature using user input and loops.
Through these tasks, I improved my understanding of Python syntax, logical thinking, and problem-solving skills.
 I also learned how to take user input, perform calculations, and display outputs effectively.

"""