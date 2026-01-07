import json
import numpy as np
import pandas as pd

"""
matrix = np.array([[1, 2, 3, 4], [12, 13, 14, 15]])
matrix *= 10
for a_vector in matrix:
    for number in a_vector:
        print(number)
    print()
"""

test_dict = {
    "name": "Michael",
    "age": "",
    "city": "New York",
    "occupation": "Fighter"
}
test_dict2 = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
s_one = pd.Series([202, 303], index=["c_two", "c_four"])
s_two = pd.Series([1001, 2002, 3003], index=["c_two", "c_three", "c_four"])

test_dict3 = {
    "calories": s_one,
    "duration": s_two
}

test_dict4 = pd.Series([pd.Series([101, 202, 303], index=["c_one", "c_two", "c_three"]), pd.Series([2002, 3003], index=["c_two", "c_three"])])

"""
first_df = pd.Series(test_dict, dtype="string")
print(first_df, end="\n\n")
print(f"'{type(first_df["age"])}'")
"""
second_df = pd.DataFrame(test_dict2, index=pd.Index(["one", "two", "three"]))
#print(second_df)

#print()

third_df: pd.DataFrame = pd.DataFrame(test_dict3)


#print()
#print()
"""
for value in csv_df:
    print(value)
    """
#print(third_df)
#print()
print(third_df.info())
print()
print(third_df.to_dict(orient='list'))
print(json.dumps(third_df.to_dict(orient='list')))
