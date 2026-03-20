import itertools
import time
from multiprocessing import Process, Event
from multiprocessing import synchronize
""" multiprocessing.Event is a function (not a class like threading.Event) which returns a synchronize.Event instance 
forcing us to import multiprocessing.synchronize and write this type hint """

def spin(msg: str, done: synchronize.Event) -> None:
    for char in itertools.cycle(r'\/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        if done.wait(.1):
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')

""" Blocks the calling thread but release the GIL so the spinner thread can proceed """
def slow() -> int:
    time.sleep(3)
    return 42

def supervisor() -> int:
    done = Event()
    spinner = Process(target=spin, args=('thinking!', done))
    print(f'spinner object: {spinner}')
    spinner.start()
    result = slow()
    done.set()
    spinner.join()
    return result

def main() -> None:
    result = supervisor()
    print(f'Answer: {result}')

if __name__ == '__main__':
    main()

"""
The basic API of threading and multiprocessing are similar, but their implementation is very different, and 
multiprocessing has a much larger API to handle the added complexity of multiprocess programming. For example, one 
challenge when converting from threads to processes is how to communicate between processes that are isolated by the 
operating system and can’t share Python objects. This means that objects crossing process boundaries have to be 
serialized and deserialized, which creates overhead. In this example, the only data that crosses the process boundary is
the Event state, which is implemented with a low-level OS semaphore in the C code underlying the multiprocessing module.
The semaphore is a fundamental building block that can be used to implement other synchronization mechanisms. Python 
provides different semaphore classes for use with threads, processes, and coroutines.

Since Python 3.8, there’s a multiprocessing.shared_memory package in the standard library, but it does not support 
instances of user-defined classes. Besides raw bytes, the package allows processes to share a ShareableList, a mutable 
sequence type that can hold a fixed number of items of types int, float, bool, and None, as well as str and bytes up to 
10 MB per item.
"""
