from schema import FinalStructure
import pandas as pd

# I stored the data as XML in a file so that it feels a little prod like
og_df: pd.DataFrame = pd.read_xml("./data.xml", parser="etree")


og_df["has_bike"] = [False, True, False]
og_df.loc[len(og_df)] = { "city": "Las Vegas", "car_company": "Ford", "age": 50,  "car_engine_type": "Diesel", "engine_capacity": 2000, "full_name": "Marc Goddard", "has_bike": True, "person_id": 4}
og_df.index = ["first", "second", "third", "forth"]
og_df.columns = ["ek", "do", "teen", "chaar", "panch", "ch_ae", "sa_at", "ah_th"]
og_df = og_df.convert_dtypes()
print(og_df, end="\n\n")
og_df.drop(og_df.columns[2], axis=1, inplace=True)
print(og_df)

"""
# grouping by people because that is what the differentiating factor is 
group_of_people = og_df.groupby("full_name")

for name, group in group_of_people:
    
    # DataFrame uses different terms for column label then what json uses for its keys, so doing a rename
    mod_group = group.rename({"person_id": "id", "full_name": "name", "car_company": "company", "car_engine_type": "engine_type", "car_capacity": "capacity"}, axis=1)
    print(mod_group.to_dict(orient="list"))
"""
