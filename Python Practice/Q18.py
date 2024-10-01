# 18) In the Kaggle insurance data set (https://www.kaggle.com/c/prudential-life-insurance-assessment/data),
# the Response column is the output variable and the rest are input variables. Perform the following: • Fill in the
# missing values applying an appropriate technique. • Make use of the insurance data set to explore the
# multicollinearity among the input variables. • Single out three input variables that are most relevant to
# predicting the output variable.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from patsy.highlevel import dmatrices
from statsmodels.stats.outliers_influence import variance_inflation_factor

df = pd.read_csv("train.csv")

# Fill in the missing values applying an appropriate technique

for i in df.columns:
    df[i].fillna(df[i].mode()[0], inplace=True)
print(f'Dataframe after filling missing values with mode of column: \n{df}')


# Make use of the insurance data set to explore the multicollinearity among the input variables.
def calc(X):
    data = pd.DataFrame()
    data["variables"] = X.columns
    data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

    return data


y, X = dmatrices('Response ~ Ins_Age+Ht+Wt+BMI+Employment_Info_1+Employment_Info_2'
                 '+Employment_Info_3+Employment_Info_4+Employment_Info_5+Employment_Info_6+InsuredInfo_1'
                 '+Insurance_History_1+Family_Hist_1+Medical_History_1+Medical_Keyword_1', data=df, return_type='dataframe')
collinearity = calc(X)
print(f'Multicollinearity of Input Variables are: \n{collinearity}\n')

# Single out three input variables that are most relevant to predicting the output variable
print(f"The most relevant inputs are: \n{collinearity.sort_values(by=['VIF'], ascending=False).head(3)}")
