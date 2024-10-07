from datetime import datetime

print("\tenter a name\rJohn")

present = datetime.now()
print(f"{present:%d-%m-%Y}")
name = "johnWick"
number = 45

"""
print(f"\nthis is the number={number:05d}.\n")
print(f"\nthe name is={name:^5}.\n")
"""
