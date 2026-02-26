# Async

## 3 important constructs:

### Construct 1
```
async def do_something_async():
    pass
```
this ↑ is a **coroutine function**. (construct 1)

### Construct 2
`do_something_async()`  ← simply calling a coroutine function, does not execute anything; instead it returns a **coroutine object**.

### Construct 3
`task = asyncio.create_task(do_something_async())`  ← this gives us a **Task**.

When we create a task, it is automatically scheduled for execution (Pedantic Speak: a callback to it has been added to the event loop's to-do list).
Important to note that tasks themselves are not in the Event Loop's to-do list, their associated callbacks are.
If the tasks are garbage collected before the event loop gets to execute their associated callback, the callback may just not be executed, hence maintaining state of tasks are important.

---- x ----

For the following program, while the event loop is executing a coroutine (some_coroutine_func())-
```
async def some_coroutine_func():
    # does something
    task = asyncio.create_task(a_coroutine_func())          # ← schedules a callback and assign a task for it.
    # some more things
    await task                          # ←--
    # executes after
```
when we are at `await task`, what does not happen is that event loop now focus on executing the callback associated with `task`. This absolutely does not happens.
What really happens is that at the await point, the current execution is paused, and the control is ceded to the event loop.
The event loop executes whatever is first, in it's ready queue, and in a FIFO order execute the tasks in ready queue. We don't control what gets executed when.
We only have one guarantee that after executing `task`, we will see the previously paused `some_coroutine_func()` resumes again for remaining execution.
NOTE: This is the main philosophy here, we don't authorize what to execute when. We just schedule stuff, and the at await points cede control to the event loop. All the authoritative powers of what to execute when sits with the event loop.

---- x ----

An awaited coroutine object is not the same as an awaited task.
A task is scheduled and when awaited, control is ceded to the event loop, and at some point, the task gets executed. Asychronous, event loop dependent.
An coroutine object, is just like a normal function call. No giving up control to the event loop, just pure function execution. This seems reverse but the process of going to the event loop is a resource heavy one especially when we are deep inside a call stack (control flows up the stack and all those function gets added to the task's callback list for later execution). Sometimes, the performance aware thing is to just call that coroutine function like a normal function call, hence this dual behaviour.
