## Method Resolution Order (MRO)

The most important factor in understanding where the `super()` will take us next.

Let's take an example.

```
class A1:
    def method(self):
        print("A1 method")

class A2:
    def method(self):
        print("A2 method")

class B(A1):
    def method(self):
        super().method()
        print("B method")

class C(A2):
    def method(self):
        super().method()
        print("C method")

class D(B, C):
    def method(self):
        super().method()
        print("D method")

d = D()

print(d.__class__.__mro__)
d.method()
```

Now here, things are a little different-
- like previously, we start with method of class D
- then, just as before, following the inheritance order `class D(B, C)`, super goes to method of **class B**
- and now, the super goes to the method of **class A1**. Why, because we have `class D(B, C)`, it processes B's entire hierarchy first.
- the MRO ends here because class A1 does not have any super() method calls that continue the flow.

D -> B -> A1 


----------


Another example-

```
class A:
    def method(self):
    print("A")

class B(A):
    def method(self):
    print("B")
    super().method()

class C(A):
    def method(self):
    print("C")
    super().method()

class D(B, C):  
    def method(self):
    print("D")
    super().method()

d = D()
d.method()
```


Here, the flow will be like this-
- since we start with d.method(), so the first method called is of the class D
- second, super go to the method of class B, this is because the in the inheritance order `class D(B, C)` B comes first.
- third, super call the method of class C. BUT WAIT! why not method of class A, following the example to process B's entire hierarchy first before moving further. This is because there is another rule that is to process all inherited class first before processing the base class. Now since both B and C has A as their common base class
- lastly, super goes to class A 

D -> B -> C -> A


