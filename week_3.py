'''Client Project: Clean and aggregate a dataset (e.g., remove missing values,
calculate averages).'''

import pandas as pd

data = {
    "Name": ["Hardik", "Rahul", "Priya", "Amit","vishal"],
    "Marks": [85, None, 88, 92, None]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Remove missing values
clean_df = df.dropna()

print("\nCleaned Dataset:")
print(clean_df)

# Calculate average marks
average_marks = clean_df["Marks"].mean()

print("\nAverage Marks:", average_marks)


"""
summary :-

In Week 3, I learned NumPy arrays, array operations, and basic numerical computations. 
I also studied Pandas DataFrames, Series, indexing, and data manipulation techniques.

I performed data operations using NumPy and worked with datasets using Pandas. 
For the client project, I cleaned a dataset by removing missing values and calculated average values from the cleaned data.

This week helped me understand how data is stored, processed, cleaned, and analyzed using Python libraries commonly used in Data Science.
"""
