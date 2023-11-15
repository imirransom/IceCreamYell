from IPython.display import display
from tabulate import tabulate
import pandas as pd

ic = pd.read_csv("ice_cream.csv")
ic.columns = ["person_id", "gender", "ice_cream_flavor", "video_game", "puzzle_game"]

if 0 in ic.gender:
    ic["gender"] = "Male"
if 1 in ic.gender:
    ic["gender"] = "Female"

icdf = pd.DataFrame(ic)

print(tabulate(icdf, headers="keys", tablefmt="psql"))

unpivot_ic = ic.groupby(["gender", "ice_cream_flavor"]) ["video_game"]

# pivoted_ic = ic.pivot(columns="ice_cream",
#                       index=
#
#                       )