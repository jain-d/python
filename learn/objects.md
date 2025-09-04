# Objects in python

Objects, which are everything, can be categorized into 2 types-

- ***Value objects***: Hold atomic values (e.g., int, float, bool). 
- ***Container objects***: Hold references to other value or reference objects (e.g., list, dict, tuple).

Container objects can be nested, holding other containers or value objects.

Only the lowest level (value objects) holds actual values.



# Shallow vs. Deep copy

- **Shallow copy (`copy.copy()`)**
  - Copies outer container only.
  - Inner objects (references) are shared.
- **Deep copy (`copy.deepcopy()`)**
  - Recursively copies all nested containers.
  - New objects created for mutable elements.
  - Immutable elements are **not duplicated**—only referenced.

- Deepcopy creates **new objects** only for **mutable types**:
  - Lists, dicts, sets, custom classes, etc.

- Deepcopy does **not duplicate** immutable elements like integers.
- Instead, it **reuses the same object reference** for immutables.
