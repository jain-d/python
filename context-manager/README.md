# Context Managers


## Philosophy
For any resource that is critical, and for which we want proper handling during and after its execution, we use context managers.
It help us write explicit code defining what should happen(what code to be executed) when we begin accessing the privileged resource, and what code should execute when we are done working that resource. Incase if there is a failure in between, while we are working with the resource, it help use write code that is to executed before our program crashes.

**Definition of critical resource**: Anything like a files, network connections, thread locks, database transactions. Anything that needs proper setup and cleanup.


## Implementation
Implementing context manager is relatively simple, any object that implements the context manager protocol, which means that any object that has an implementation of the `__enter__()` and `__exit__()` method, that is now a context manager. Half of the work is done.

The other half, is we consume a context manager using the `with` keyword.

**Modern Implementation**
Context manager are implemented in functional manner, where the `@contextmanager` decorator is used. It make the function that is decorated a generator function, with code before yield running as setup, yield being the context managed operation(both of these enclosed in a try), and after it as clean-up(enclosed in finally). This method is much more elegant while doing the same thing.


**NOTE**: At the end of it all, context managers are just a nicer, more elegant abstraction over a series of try/catch/finally statements.
