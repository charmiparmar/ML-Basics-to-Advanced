# 15) Read the loan data file into a dataframe and then compute the following:
# • mean and variance of the Age column,
# • correlation coefficient between the two numerical columns Age and Time_at_address,
# • the conditional probability p(Decision = reject | Occupation = Unemployed),
# • frequency of values in the Job-status column and then draw a bar diagram using matplotlib.

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel("loan.xlsx")

# find mean and variance
mean = df["Age"].mean()
print(f'Mean: {mean}\n')

var = df["Age"].var()
print(f'Variance: {var}\n')

# correlation coefficient
coefficient = df["Age"].corr(df["Time_at_address"])
print(f'Correlation coefficient: \n{coefficient}\n')

# conditional probability p(Decision = reject | Occupation = Unemployed),
num_of_unemp_and_reject = len(df.loc[(df['Job_status'] == 'unemploye') & (df['Decision'] == 'reject')])
num_of_unemp = len(df.loc[df['Job_status'] == 'unemploye'])

cond_prob = num_of_unemp_and_reject/num_of_unemp
print(f'Conditional Probablitiy is: {cond_prob}\n')

# frequency of values in the Job-status column and then draw a bar diagram using matplotlib
freq = df['Job_status'].value_counts()
print(f'Frequency of Job Status: {freq}')

ax = plt.subplot()
ax.bar(df["Age"], df["Occupation"])
ax.bar(df["Age"], df["Occupation"], color="maroon")
plt.title('Frequency of Job Status')
plt.show()
