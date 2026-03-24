import sys
from time import perf_counter
from typing import NamedTuple
from multiprocessing import Process, SimpleQueue, cpu_count
from multiprocessing import queues
from utils import is_prime, NUMBERS

class PrimeResult(NamedTuple):
    n: int
    prime: bool
    elapsed: float

def check(n: int) -> PrimeResult:
    t0 = perf_counter()
    prime = is_prime(n)
    return PrimeResult(n, prime, perf_counter() - t0)

jobQueue = SimpleQueue[int]
resultQueue = SimpleQueue[PrimeResult]

def worker(jobs: jobQueue, results: resultQueue) -> None:
    while n:= jobs.get():
        results.put(check(n))
    results.put(PrimeResult(0, False, 0.0))

def start_jobs(procs: int, jobs: jobQueue, results: resultQueue) -> None:
    for num in NUMBERS:
        jobs.put(num)

    for _ in range(procs):
        proc = Process(target=worker, args=(jobQueue, results))
        proc.start()
        proc.put(0)

"""
Trying to emulate threading, multiprocessing provides multiprocessing.SimpleQueue, but this is a method bound to a 
predefined instance of a lower-level BaseContext class. We must call this SimpleQueue to build a queue, we can’t use it
in type hints.

"""