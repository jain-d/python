import pandas as pd
from schema import Item, Object, FinalStructure


df = pd.DataFrame({
    "order_id": [101, 101, 102, 103, 103, 103],
    "customer_name": ["Alice", "Alice", "Bob", "Charlie", "Charlie", "Charlie"],
    "item_name": ["Apples", "Oranges", "Bread", "Milk", "Biscuits", "Cheese"],
    "quantity": [3, 2, 1, 2, 4, 1],
    "price": [1.2, 1.0, 2.5, 1.1, 0.8, 3.5],
})

ordered_df: pd.DataFrame = df.groupby(["order_id", "customer_name"]).apply(lambda x: x[["item_name", "quantity", "price"]].rename(columns={"item_name": "name", "quantity": "qty"}).to_dict(orient="records"), include_groups=False).reset_index(name="items")

list_of_objects: list[Object] = []
for _, row in ordered_df.iterrows():
    items: list[Item] = []
    for item in row["items"]:
        items.append(Item(**item))
    list_of_objects.append(Object(orderId=row["order_id"], customer=row["customer_name"], items=items))

final_struct = FinalStructure(orders=list_of_objects)
print(final_struct.model_dump_json())
