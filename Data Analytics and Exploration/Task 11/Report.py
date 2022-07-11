import pandas as pd

df = pd.read_csv('balance.txt', delim_whitespace=True)

# The average income based on ethnicity
ethnicity_grouped = df.groupby(['Ethnicity']).mean()
print(ethnicity_grouped.loc[:,"Income"])

# On average, do married or single people have a higher balance?
married_grouped = df[df.Married == "Yes"].loc[:,"Balance"].mean()
unmarried_grouped = df[df.Married == "No"].loc[:,"Balance"].mean()
if married_grouped > unmarried_grouped:
    print('Married have a higher balance on average')
else:
    print('Single people have a higher balance on average')

# What is the highest income in our dataset
print("The highest income in our dataset is:", df.loc[:, "Income"].max())

# What is the lowest income in our dataset?
print("The lowest income in our dataset is:", df.loc[:, "Income"].min())

# How many cards do we have recorded in our dataset
print("The amount of cards recorded in our dataset is:", df.loc[:, "Cards"].sum())

# How many females do we have information for vs how many males?
print("Number of females in our dataset:", df[df.Gender == "Female"].loc[:,"Gender"].count())
print("Number of males in our dataset:", df[df.Gender == " Male"].loc[:,"Gender"].count())