import lxml
import numpy as np
import pandas as pd


og_df: pd.DataFrame = pd.read_csv("./impure.csv")

small_df: pd.DataFrame = og_df.iloc[:10]
small_df = small_df.set_axis(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"], axis="index")

print(small_df, end="\n\n")
mask = small_df["Duration"] == 45
print(type(mask))
