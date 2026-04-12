import time
from pathlib import Path
from typing import Callable
import math

import httpx


POP20_CC = 'CN IN US ID BR PK NG BD RU JP MX PH VN ET EG DE IR TR CD FR'.split()
BASE_URL = 'https://www.fluentpython.com/data/flags'
DEST_DIR = Path('downloaded')

def save_flag(img: bytes, filename: str) -> None:
    (DEST_DIR / filename).write_bytes(img)

def get_flag(cc: str) -> bytes:
    url = f'{BASE_URL}/{cc}/{cc}.gif'.lower()
    resp = httpx.get(url, timeout=6.1, follow_redirects=True)
    resp.raise_for_status()
    return resp.content

def main(downloader: Callable[[list[str]], int]) -> None:
    DEST_DIR.mkdir(exist_ok=True)
    t0 = time.perf_counter()
    count = downloader(POP20_CC)
    elapsed = time.perf_counter() - t0
    print(f'\n{count} downloads in {elapsed:.2f}s')

NUMBERS = (
    2,
    142702110479723,
    299593572317531,
    3333333333333301,
    3333333333333333,
    3333335652092209,
    4444444444444423,
    4444444444444444,
    4444444488888889,
    5555553133149889,
    5555555555555503,
    5555555555555555,
    6666666666666666,
    6666666666666719,
    6666667141414921,
    7777777536340681,
    7777777777777753,
    7777777777777777,
    9999999999999917,
    9999999999999999,
)

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    root = math.isqrt(n)
    for i in range(3, root + 1, 2):
        if n % i == 0:
            return False
    return True