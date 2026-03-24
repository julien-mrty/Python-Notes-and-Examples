import math
import itertools
from threading import Thread, Event

NUMBERS = 5_000_111_000_222_021
""" 
is_prime blocks the calling thread and doesn't release the GIL !!!
BUT, Python suspends the running thread every 5ms, making the GIL available to other pending threads.
Therefore, the main thread running is_prime is interrupted every 5ms, allowing the secondary thread to wake up and 
iterate once through the for loop, until it calls the wait method of the done event, at which time it will release the 
GIL. The main thread will then grab the GIL, and the is_prime computation will proceed for another 5ms.

We got away with a compute-intensive task using threading in this simple experiment because there are only two threads: 
one hogging the CPU, and the other waking up only 10 times per second to update the spinner. But if you have two or more
threads vying for a lot of CPU time, your program will be slower than sequential code.
"""
def spin(msg: str, done: Event) -> None:
    for char in itertools.cycle(r'\/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        if done.wait(.1):
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')

def supervisor() -> int:
    done = Event()
    spinner = Thread(target=spin, args=('thinking!', done))
    print(f'spinner object: {spinner}')
    spinner.start()
    result = is_prime(NUMBERS)
    done.set()
    spinner.join()
    return result

def main() -> None:
    result = supervisor()
    print(f'Answer: {result}')

if __name__ == '__main__':
    main()
