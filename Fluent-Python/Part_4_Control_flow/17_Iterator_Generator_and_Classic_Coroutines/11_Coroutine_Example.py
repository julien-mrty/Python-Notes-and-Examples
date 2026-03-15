from collections.abc import Generator

def averager() -> Generator[float, float, None]:
    total = 0.0
    count = 0
    average = 0.0
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count

"""
This function returns a generator that yields float values, accepts float values via .send(), and does not return a 
useful value. In fact, it never returns unless some exception breaks the loop. Mypy 0.910 accepts both None and 
typing.NoReturn as the generator return type parameter, but it also accepts str in that position, so apparently it can’t
fully analyze the coroutine code at this time.

This infinite loop means the coroutine will keep on yielding averages as long as the client code sends values.
The yield statement here suspends the coroutine, yields a result to the client, and—later—gets a value sent by the 
caller to the coroutine, starting another iteration of the infinite loop.

In a coroutine, total and count can be local variables: no instance attributes or closures are needed to keep the 
context while the coroutine is suspended waiting for the next .send(). That’s why coroutines are attractive replacements
for callbacks in asynchronous programming, they keep local state between activations.
"""

coro_avg = averager()
# coro_avg.send(20) TypeError: can't send non-None value to a just-started generator
# next(coro_avg)
coro_avg.send(None)
print(coro_avg.send(10))
print(coro_avg.send(30))
print(coro_avg.send(5))
"""
Create the coroutine object.
Start the coroutine. This yields the initial value of average: 0.0.
Now we are in business: each call to .send() yields the current average.

The call next(coro_avg) makes the coroutine advance to the yield, yielding the initial value for average. You can also 
start the coroutine by calling coro_avg.send(None), this is actually what the next() built-in does. But you can’t send 
any value other than None, because the coroutine can only accept a sent value when it is suspended at a yield line. 
Calling next() or .send(None) to advance to the first yield is known as “priming the coroutine.”

After each activation, the coroutine is suspended precisely at the yield keyword, waiting for a value to be sent. The 
line coro_avg.send(10) provides that value, causing the coroutine to activate. The yield expression resolves to the 
value 10, assigning it to the term variable. The rest of the loop updates the total, count, and average variables. The 
next iteration in the while loop yields the average, and the coroutine is again suspended at the yield keyword.

The attentive reader may be anxious to know how the execution of an averager instance (e.g., coro_avg) may be 
terminated, because its body is an infinite loop. We don’t usually need to terminate a generator, because it is garbage 
collected as soon as there are no more valid references to it. If you need to explicitly terminate it, use the .close() 
method
"""

coro_avg.send(20)
coro_avg.close()
coro_avg.close()
coro_avg.send(5)
"""
The .close() method raises GeneratorExit at the suspended yield expression. If not handled in the coroutine function, 
the exception terminates it. Generator Exit is caught by the generator object that wraps the coroutine—that’s why we
don’t see it. Calling .close() on a previously closed coroutine has no effect. Trying .send() on a closed coroutine 
raises StopIteration.
"""