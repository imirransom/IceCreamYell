from IPython.display import display
from tabulate import tabulate
import pandas as pd

# Reading the CSV file using the pandas module
ic = pd.read_csv("ice_cream.csv")
# print(ic.head(10))
# Changed all column names using the column method so that they are more clear
ic.columns = ["person_id", "gender", "ice_cream_flavor", "video_game_score", "puzzle_game_score"]
# I replaced the 0 and 1 contents in the gender column to say male and female using the replace method
ic['gender'] = ic['gender'].replace({0: 'male', 1: 'female'})
# Used the replace method to display the flavored ice cream rather than the numbers 1, 2, and 3
ic["ice_cream_flavor"] = ic["ice_cream_flavor"].replace({1: 'vanilla', 2: 'chocolate', 3: "strawberry"})
# set a variable to hold the dataframe method being used on the csv file ic
icdf = pd.DataFrame(ic)
print("Info on ice cream table\n")
print("-------------------------------------------------")
print(ic.info())
print("-------------------------------------------------\n")
# Using the tabulate library that takes a Pandas DataFrame as the first parameter, the second parameter the header: it
# takes the column names (keys) and uses them as headers in the table and the third parameter specifies the format
# of the table which is set to "psql"
def to_tabulate(df, format):
    print(tabulate(df, headers="keys", tablefmt=format))

# print(tabulate(icdf.head(20), headers="keys", tablefmt="psql"))


to_tabulate(icdf.head(20), "psql")



ic_by_gender = ic.groupby("gender").puzzle_game_score.mean()
icdf2 = pd.DataFrame(ic_by_gender)
to_tabulate(icdf, "psql")
to_tabulate(icdf2, "psql")

# unpivot_ic = ic.groupby(["gender", "person_id"])["video_game_score"].mean().reset_index()
#
# pivoted_ic = unpivot_ic.pivot(
#     columns="person_id",
#     index="gender",
#     values="video_game_score"
# )
#
# print(tabulate(pivoted_ic, headers="keys", tablefmt="psql"))

