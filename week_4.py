"""
Client Project: Create a dashboard for visualizing relationships between
features in a dataset (e.g., scatter plots, histograms).
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Hours_Studied": [2, 3, 4, 5, 6, 7, 8],
    "Marks": [50, 60, 70, 75, 85, 95, 98]
}

df = pd.DataFrame(data)

# Scatter Plot
plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x="Hours_Studied", y="Marks")
plt.title("Hours Studied vs Marks")
plt.show()

# Histogram
plt.figure(figsize=(8,5))
plt.hist(df["Marks"], bins=5)
plt.title("Marks Distribution")
plt.show()

"""
In Week 4, I learned data visualization techniques using Matplotlib and Seaborn. 
I studied different types of plots such as bar charts, histograms, scatter plots, 
and explored how visualizations help in understanding data patterns and relationships.

For the hands-on activities, I created visualizations to analyze datasets. 
In the client project, I developed a simple dashboard using scatter plots and 
histograms to visualize the relationship between study hours and student marks.

This week improved my ability to present data visually, identify trends, 
and communicate insights effectively using Python visualization libraries.
"""