from IPython.display import display
from tabulate import tabulate
import pandas as pd

ic = pd.read_csv("ice_cream.csv")
ic.columns = ["person_id", "gender", "ice_cream_flavor", "video_game", "puzzle_game"]

ic['gender'] = ic['gender'].replace({0: 'male', 1: 'female'})
ic["ice_cream_flavor"] = ic["ice_cream_flavor"].replace({1: 'vanilla', 2: 'chocolate', 3: "strawberry"})
icdf = pd.DataFrame(ic)

print(tabulate(icdf, headers="keys", tablefmt="psql"))

unpivot_ic = ic.groupby(["gender", "ice_cream_flavor"]) ["video_game"]

# pivoted_ic = ic.pivot(columns="ice_cream",
#                       index=
#
#                       )