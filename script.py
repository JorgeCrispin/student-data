# Load libraries
import pandas as pd
import numpy as np
import codecademylib3
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
students = pd.read_csv('students.csv')

# Print first few rows of data
print(students.head())
# Print summary statistics for all columns
print(students.describe(include='all'))
# Calculate mean
mean_grade = students.math_grade.mean()
print("Average grade: ",mean_grade)
# Calculate median
med_grade = students.math_grade.median()
print('Median grade: ',med_grade)
# Calculate mode
mode_grade = students.math_grade.mode()
print('Mode grade: ',mode_grade)
# Calculate range
the_range = students.math_grade.max()-students.math_grade.min()
print("Grade Range: ", the_range)
# Calculate standard deviation
MathGrade_dev = students.math_grade.std()
print('Standard Deviation: ',MathGrade_dev)
# Calculate MAD
The_mad = students.math_grade.mad()
print('The mean absolute deviation: ', round(The_mad))
# Create a histogram of math grades

sns.histplot(x='math_grade', data=students)
plt.show()
plt.clf()

# Create a box plot of math grades

sns.boxplot(x='math_grade',data=students)
plt.show()
plt.clf()

# Calculate number of students with mothers in each job category
mom_job = students.Mjob.value_counts()
print('Mother job type:\n',mom_job)
# Calculate proportion of students with mothers in each job category
mom_job_prop = students.Mjob.value_counts(normalize=True)
print("Poportion (percent) of the mother's jobs:\n",round(mom_job_prop,2)*100)
# Create bar chart of Mjob

sns.countplot(x='Mjob',data=students)
plt.show()
plt.clf()

# Create pie chart of Mjob

students.Mjob.value_counts().plot.pie()
plt.show()
plt.clf()

# Calculate number of students with Fathers in each job category
pop_job = students.Fjob.value_counts()
print('Father job type:\n',pop_job)
# Calculate proportion of students with Fathers in each job category
pop_job_prop = students.Fjob.value_counts(normalize=True)
print("Poportion (percent) of the Father's jobs:\n", pop_job_prop*100)
# Create bar chart of Fjob

sns.countplot(x='Fjob',data=students)
plt.show()
plt.clf()

# Create pie chart of Fjob

students.Fjob.value_counts().plot.pie()
plt.show()
plt.clf()