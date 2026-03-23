import asyncio
import itertools
import time
"""
It is the job of OS schedulers to allocate CPU time to drive threads and processes. In contrast, coroutines are driven 
by an application-level event loop that manages a queue of pending coroutines, drives them one by one, monitors events 
triggered by I/O operations initiated by coroutines, and passes control back to the corresponding coroutine when each 
event happens. The event loop and the library coroutines and the user coroutines all execute in a single thread. 
Therefore, any time spent in a coroutine slows down the event loop—and all other coroutines.
"""

async def spin(msg: str) -> None:
    for char in itertools.cycle(r'\/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        try:
            await asyncio.sleep(0.001) # spin wakes up every millisecond
        except asyncio.CancelledError:
            break

    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')

""" Blocks the calling thread but release the GIL so the spinner thread can proceed """
async def slow() -> int:
    """ # Ex: make an http call. Well-designed network libraries are async, therefore they release the GIL. """
    await asyncio.sleep(3)
    #time.sleep(3) # Doesn't release the GIL
    return 42

async def supervisor() -> int:
    spinner_task = asyncio.create_task(spin("Thinking!"))
    print(f'spinner object: {spinner_task}')
    result = await slow()
    spinner_task.cancel()
    return result

def main() -> None:
    result = asyncio.run(supervisor())
    print(f'Answer: {result}')

if __name__ == '__main__':
    main()
