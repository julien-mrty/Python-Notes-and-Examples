""""""
from asyncio import Event
from typing import Iterator, Generator

"""
Generator are commonly used as iterators, but they can also be used as coroutines. A coroutine is really a generator
function, created with the yield keyword in its body. And a coroutine object is physically a generator object. Despite 
sharing the same underlying implementation in C, the use cases of generators and coroutines in Python are so different 
that there are two ways to type hint them:
"""
# The `readings` variable can be bound to an iterator
# or generator object that yields `float` items:
readings: Iterator[float]
# The `sim_taxi` variable can be bound to a coroutine
# representing a taxi cab in a discrete event simulation.
# It yields events, receives `float` timestamps, and returns
# the number of trips made during the simulation:
sim_taxi: Generator[Event, float, int]

"""
The typing documentation describes the formal type parameters of Generator like this:
Generator[YieldType, SendType, ReturnType]
The SendType is only relevant when the generator is used as a coroutine. That type parameter is the type of x in the 
call gen.send(x). It is an error to call .send() on a generator that was coded to behave as an iterator instead of a 
coroutine. Likewise, ReturnType is only meaningful to annotate a coroutine, because iterators don’t return values like 
regular functions. The only sensible operation on a generator used as an iterator is to call next(it) directly or 
indirectly via for loops and other forms of iteration. The YieldType is the type of the value returned by a call to 
next(it).

The Generator type has the same type parameters as typing.Coroutine:
Coroutine[YieldType, SendType, ReturnType]
The typing.Coroutine documentation actually says: “The variance and order of type variables correspond to those of 
Generator.” But typing.Coroutine (deprecated) and collections.abc.Coroutine (generic since Python 3.9) are intended to 
annotate only native coroutines, not classic coroutines. If you want to use type hints with classic coroutines, you’ll 
suffer through the confusion of annotating them as Generator[YieldType, SendType, ReturnType].

Keeping It Straight:
• Generators produce data for iteration
• Coroutines are consumers of data
• To keep your brain from exploding, don’t mix the two concepts together
• Coroutines are not related to iteration
• Note: There is a use of having `yield` produce a value in a coroutine, but it’s not tied to iteration.
"""