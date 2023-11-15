from IPython.display import display
import pandas as pd

icdb = pd.read_csv("ice_cream.csv")
ic = pd.DataFrame(icdb)

print(ic.style)
