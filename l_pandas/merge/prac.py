import numpy as np
import pandas as pd

"""
df = pd.DataFrame({
    "team": ["A", "A", "A", "B", "B"],
    "player": ["p1", "p2", "p3", "p4", "p5"],
    "score": [10, 15, 12, 20, 25]
})

mod_df = df.groupby("team").agg(player_list=("player", list), avg_score=("score", "mean"), player_count=("player", "count")).reset_index()

print(mod_df)
"""

"""
df_2 = pd.DataFrame({
    "dept": ["IT", "IT", "HR", "HR", "HR", "Finance"],
    "salary": [80, 90, 60, 65, 70, 100]
})

mod_df2 = df_2.groupby("dept").agg(min_salary=("salary", "min"), max_salary=("salary", "max"), avg_salary=("salary", "mean"), count=("salary", "count")).sort_index().reset_index()

print(mod_df2)
"""

df_3 = pd.DataFrame({
    "category": ["Fruit", "Fruit", "Fruit", "Veg", "Veg"],
    "item": ["Apple", "Banana", "Mango", "Carrot", "Spinach"],
    "price": [100, 40, 90, 30, 25],
    "quantity": [50, 80, 40, 100, 60]
})

mod_df3 = df_3.groupby("category").agg(items_list=("item", list), total_quantity=("quantity", "sum"), avg_price=("price", "mean")).reset_index()

print(mod_df3, end="\n\n")


mod_df4 = df_3.groupby("category").agg(min_price=("price", "min"), max_price=("price", "max"), avg_price=("price", "mean"), total_quantity=("quantity", "sum"), item_count=("item", "count")).reset_index()

print(mod_df4)

df5 = df_3.copy()
#mod_df5 = df_3.groupby("category").agg(lambda x: {"min_price": x["price"].min(), "max_price": x["price"].max(), "count": x["item"].count()}).reset_index()
#df5 = df5.groupby("category").agg(summary=(["price", "item"], [["max", "min"], "count"]))
#df5 = df5.groupby("category")[["item", "price"]].agg(lambda x: dict(max_price=x["price"].max(), min_price=x["price"].min(), count=x["item"].count()))
#df5 = df5.groupby("category").apply(lambda g: {"min_price": g["price"].min(), "max_price": g["price"].max(), "count": g["item"].count()}).reset_index(name="summary")
df5 = df5.groupby("category", as_index=False).agg(summary=("price", lambda p: dict(min_index=p.min(), max_index=p.max(), count=p.count())))
print(df5, end="\n\n")

df_4 = pd.DataFrame({
    "order_id": [100, 100, 100, 101, 101],
    "item": ["Pen", "Notebook", "Book", "Tablet", "Cover"],
    "price": [10, 20, 15, 200, 20],
    "qty": [1, 2, 1, 1, 1]
})

#mod_df6 = df_4.groupby("order_id").agg(items=lambda g: g[["item", "price", "qty"]].to_dict("records"))
result = (
df_4.groupby("order_id")
    .apply( lambda g: g[["item", "price", "qty"]].to_dict("records"))
    .reset_index(name="items"))
print(result)
