from IPython.display import display
from tabulate import tabulate
import pandas as pd

# Reading the CSV file using the pandas module
ic = pd.read_csv("ice_cream.csv")
print(ic.head(20))
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

# I made a tabulate function that will take a dataframe and table format as a parameter
def to_tabulate(df, format):
    print(tabulate(df, headers="keys", tablefmt=format))

# print(tabulate(icdf.head(20), headers="keys", tablefmt="psql"))


to_tabulate(ic.head(20), "psql")

# This will group up the columns gender and game scores and show the average of how males and females differ
print("-------------------------------------------------")
print("\nAVERAGE PUZZLE GAME SCORE")
puzzle_ic_by_gender = ic.groupby("gender").puzzle_game_score.mean().reset_index()

to_tabulate(puzzle_ic_by_gender, "psql")
print("-------------------------------------------------\n")

print("AVERAGE VIDEO GAME SCORES")
video_avg_by_gender = ic.groupby("gender").video_game_score.mean().reset_index()
to_tabulate(video_avg_by_gender, "psql")
print("\n-------------------------------------------------")

print("MINIMUM PUZZLE SCORES BASED ON GENDER AND ICE CREAM FLAVOR")
min_ice_cream_by_gender = ic.groupby(["gender", "ice_cream_flavor"]).puzzle_game_score.min().reset_index()
to_tabulate(min_ice_cream_by_gender, "psql")

print("\n-------------------------------------------------")
print("MAXIMUM PUZZLE SCORES BASED ON GENDER AND ICE CREAM FLAVOR")
max_ice_cream_by_gender = ic.groupby(["gender", "ice_cream_flavor"]).puzzle_game_score.max().reset_index()
to_tabulate(max_ice_cream_by_gender, "psql")

print("\n-------------------------------------------------")
print("AVERAGE PUZZLE SCORES BASED ON GENDER AND ICE CREAM FLAVOR")
avg_ice_cream_by_gender = ic.groupby(["gender", "ice_cream_flavor"]).puzzle_game_score.mean().reset_index()
to_tabulate(avg_ice_cream_by_gender, "psql")

pivoted_average_ice_score = avg_ice_cream_by_gender.pivot(
    columns="ice_cream_flavor",
    index="gender",
    values="puzzle_game_score"
)
print("\n-------------------------------------------------")
print("PIVOTED TABLE SHOWING AVERAGE PUZZLE GAME SCORES BASED ON ICE CREAM AND GENDER")
to_tabulate(pivoted_average_ice_score.reset_index(), "psql")


# unpivot_ic = ic.groupby(["gender", "person_id"])["video_game_score"].mean().reset_index()
#
# pivoted_ic = unpivot_ic.pivot(
#     columns="person_id",
#     index="gender",
#     values="video_game_score"
# )
#
# print(tabulate(pivoted_ic, headers="keys", tablefmt="psql"))

