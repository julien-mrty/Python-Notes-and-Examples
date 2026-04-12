import sys
from concurrent import futures
from time import perf_counter
from typing import NamedTuple
from utils import is_prime, NUMBERS


class PrimeResult(NamedTuple):
    n: int
    flag: bool
    elapsed: float

def check(n: int) -> PrimeResult:
    t0 = perf_counter()
    res = is_prime(n)
    return PrimeResult(n, res, perf_counter() - t0)

def main() -> None:
    if len(sys.argv) < 2:
        workers = None
    else:
        workers = int(sys.argv[1])

    executor = futures.ProcessPoolExecutor(workers)
    actual_workers = executor._max_workers # type: ignore

    print(f'Checking {len(NUMBERS)} numbers with {actual_workers} processes:')

    t0 = perf_counter()
    numbers = sorted(NUMBERS, reverse=True)
    # numbers = NUMBERS

    with executor:
        for n, prime, elapsed in executor.map(check, numbers):
            label = 'P' if prime else ' '
            print(f'{n:16} {label} {elapsed:9.6f}s')

    time = perf_counter() - t0
    print(f'Total time: {time:.2f}s')

if __name__ == '__main__':
    main()


"""
Why does the output blocks after the first line, then print all results at the same time?
• As mentioned before, executor.map(check, numbers) returns the result in the same order as the numbers are given.
• By default, our program uses as many workers as there are CPUs, it’s what ProcessPoolExecutor does when max_workers is 
  None.
• Because we are submitting numbers in descending order, the first is 9999999999999999; with 9 as a divisor, it returns 
  quickly.
• The second number is 9999999999999917, the largest prime in the sample. This will take longer than all the others to 
  check.
• Meanwhile, the remaining processes will be checking other numbers, which are either primes or composites with large 
  factors, or composites with very small factors.
• When the worker in charge of 9999999999999917 finally determines that’s a prime, all the other processes have 
  completed their last jobs, so the results appear immediately after.
"""