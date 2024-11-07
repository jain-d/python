# Dictionaries, in python are the exact equivalent of objects in javascript.
dic = {
    "name": "John Wick",
    "age": 43,
    "city": "New York",
}


list_of_dic = [
    {
        "name": "John Wick",
        "age": 50,
        "city": "London"
    },
    {
        "name": "James Bond",
        "age": 43,
        "city": "London"
    },
    {
        "name": "Ethan Hunt",
        "age": 38,
        "city": "..."
    }
]

for content in list_of_dic:
    print(f"{content["name"]} operates in {content["city"]}")
