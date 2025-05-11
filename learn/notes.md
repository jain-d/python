### 

## About the language

- Everything in Python is an object of a particular class.

- Some objects are mutable (Lists, Dictionaries, Sets, User-Defined Classes), and some are immutable (Integers, Floats, Strings, Tuples, Booleans, Frozen Sets).

- Variables in Python are names bound to objects. Internally, these names point to memory addresses where the objects reside — but unlike pointers in C/C++, Python does not expose or manipulate these addresses directly.

- When we assign a value to a variable in Python, what happens behind the scenes is:
    1. An object of a specific type is created on the **heap**.
    2. The variable name is bound to the memory address of that object.

- Since everything is an object, everything lives on the **heap** memory.

- Python has **Call by Object Reference** semantics:
    - When passing arguments to a function, the reference to the object (not the value or the variable name itself) is passed.
    - If the object is **immutable**, changes inside the function won't affect the original object.
    - If it's **mutable**, in-place changes will reflect outside the function.

- The Python interpreter is a compiled C program that uses both the **stack** (for native C function calls) and the **heap** (where Python objects and Python-level stack frames are stored).

- Even the so-called **"Python call stack"** — a sequence of `PyFrameObject` instances used to manage function calls — is allocated on the **heap** as a chain of frame objects, not on the native call stack.

- Since everything is an object, each object carries **metadata** stored in its header, such as:
    - **Reference Count** – how many names point to this object. If this falls to zero, the object becomes eligible for garbage collection.
    - **Type Pointer** – a pointer to the object’s type (which is itself an object).
    - **Data** – the actual content of the object.
    - **Flags** – other implementation-specific metadata.

- On a lower level, every Python object is an extension of a C structure called `PyObject`.

- Python uses a **Garbage Collector**:
    - Primarily based on reference counting.
    - Also includes a **cyclic garbage collector** to detect and clean up reference cycles (e.g., self-referencing objects).

> **NOTE**: All this applies to **CPython** (the standard Python implementation). Other implementations like **PyPy** use different internal mechanisms.


RAW-
## About the language
- Everything in python is an object of a particular class
- Since everything is an object, everything live on the **HEAP** memory
- The Python interpreter is a compiled C program that uses both the stack (for function calls) and the heap (for Python Stack & objects are stored).
- Even the so-called 'Python call stack'—a sequence of PyFrameObject instances used to manage function calls—is allocated on the heap as a contiguous chain of frame objects.
- When we assign a value to a variable in python, what is happening behind the scenes is that an object of a type is created first on the heap, then the memory address of the object in being assigned to the variable.
- Variables in Python are names bound to objects. Internally, these names point to memory addresses where the objects reside — but unlike pointers in C/C++, Python does not expose or manipulate these addresses directly.
- Some objects are mutable(Lists, Dictionary, Sets & User Defined Classes), some are not(Integers, Floats, Strings, Tuples, Boolean, Frozen Sets).
- Since the variables are just references(i.e. holds memory addresses) to actual object values on the heap, Python has **Call by Object Reference**. Wherein when a value is passed as an argument, it is not call by value, it is also not call by call by reference, it is call by object reference where the value passed is the reference(address) to the object lives on on the heap. Now any modifications to that parameter in the function body does not affect the original argument if the object passed is an immutable type, else the actual object on the heap is modified.
- Since everything is an object, the object has headers which store METADATA about the object such as the (a)Reference Count, (b)Type Pointer, (c)Data (d)some other flags.
    - **Reference Count** is the count of the number of times a particular object has been referenced. If this falls to zero, then the object is garbage collected.
    - **Type Pointer** is the pointer that points to the data type, which is a type object, of the object.
    - **Data** this is exactly where the data is stored.
- On a lower level, the object extends a C structure called PyObject.
- GC; apart from using the reference count as a metric for garbage collection, python also uses cyclic garbage collector for detecting reference cycles(self-referencing structures).

NOTE: All this is with respect to CPython. PyPy has different ways of doing things.


