# 16) Suppose the loan data file provides some examples of applications to accept or reject, as specified in the
# Decision column N, given the input background info in columns A-M. Come up with various ways to find out the degree
# of relevance between each input “categorical” column of A-M and the Decision column N. (hint. Chi-Square Test of
# Independence and Mutual Information)

import pandas as pd
from scipy.stats import chi2_contingency

df = pd.read_excel("loan.xlsx")

cols = list(df.columns)
cols.pop(-1)

for col in cols:
    cont_table = pd.crosstab(df[col], df["Decision"])
    chi2, p, dof, expected = chi2_contingency(cont_table)
    print(f"{col} vs Decision: \nchi-score={chi2}, p-value={p}\n")
