import pandas as pd


df: pd.DataFrame = pd.DataFrame({
    "category": ["Fruit", "Fruit", "Fruit", "Veg", "Veg"],
    "item": ["Apple", "Banana", "Mango", "Carrot", "Spinach"],
    "price": [100, 40, 90, 30, 25],
    "quantity": [50, 80, 40, 100, 60]
})

df3 = df.copy()

df3 = df3.groupby("category").agg(items_list=("item", list), total_quantity=("quantity", "sum"), avg_price=("price", "mean")).reset_index()
print(df3, end="\n\n")

df4 = df.copy()
df4 = df4.groupby("category").agg(min_price=("price", "min"), max_price=("price", "max"), avg_price=("price", "mean"), total_quantity=("quantity", "sum"), item_count=("item", "count")).reset_index()
print(df4, end="\n\n")

df5 = df.copy()
#df5 = df5.groupby("category").agg(summary=(["price", "item"], [["max", "min"], "count"]))
#df5 = df5.groupby("category")[["item", "price"]].agg(lambda x: dict(max_price=x["price"].max(), min_price=x["price"].min(), count=x["item"].count()))
#df5 = df5.groupby("category").apply(lambda g: {"min_price": g["price"].min(), "max_price": g["price"].max(), "count": g["item"].count()}).reset_index(name="summary")
df5 = df5.groupby("category", as_index=False).agg(summary=("price", lambda p: dict(min_index=p.min(), max_index=p.max(), count=p.count())))
print(df5)
"""
df5 = df5.groupby("category", as_index=False).agg(min_price=("price", "min"),max_price=("price", "max"), count=("item", "count"))
df5 = df5.apply(lambda row: row.to_dict(), axis=1).reset_index(name="summary")
print(df5)
"""
