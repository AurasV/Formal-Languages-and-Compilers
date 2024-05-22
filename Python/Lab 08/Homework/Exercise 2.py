import pandas as pd

data = pd.read_csv("HW8Ex2.txt", header=None, names=["LastName", "FirstName", "HiringDate", "Salary"])
data.to_excel("HW8Ex2.xlsx", index=False)
