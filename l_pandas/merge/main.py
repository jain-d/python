import pandas as pd


# One-to-many operation
"""
df1 = pd.DataFrame({"cust_id": [1, 2], "name": ["Alice", "Bob"]})
df2 = pd.DataFrame({"id": [1, 1, 2], "product": ["Book", "Pen", "Laptop"]})

print(df1, end="\n\n")
print(df2, end="\n\njoined-\n")
df_join = pd.merge(df1, df2, how="inner", left_on="cust_id", right_on="id")
print(df_join)
"""


# Many-to-many operation
"""
df_one = pd.DataFrame({"key": ["A", "A", "B"], "X": [1, 2, 3]})
df_two = pd.DataFrame({"key": ["A","A","A", "B"], "Y": ["u", "v", "w", "z"]})
print(df_one, end="\n\n")
print(df_two, end="\n\njoined-\n")
df_join = pd.merge(df_two, df_one, on="key", how="inner")
print(df_join)
"""


orders = pd.DataFrame({"order_id": [100, 101, 102], "customer": ["Alice", "Bob", "Alice"]})
items = pd.DataFrame({"order_id": [100, 100, 101, 102, 102, 102], "item": ["Pen", "Book", "Tablet", "Mouse", "Keyboard", "Pad"]})

merged = orders.merge(items, how="left", on="order_id")
print(merged, end="\n\n")


g = merged.groupby("order_id")["item"].agg(list)

print(g)
