import pandas as pd #imports pandas module as pd to use pandas commands with the alias of pd

# creates dataframe of netflix data
df = pd.read_csv (r'assets/netflix_titles.csv')
print(df)

tv_ratings = pd.DataFrame(df, columns=['rating'])
print(tv_ratings.value_counts())
