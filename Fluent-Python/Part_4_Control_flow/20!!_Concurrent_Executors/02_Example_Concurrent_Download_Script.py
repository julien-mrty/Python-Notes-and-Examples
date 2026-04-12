from concurrent import futures

from utils import get_flag, save_flag, main

def download_one(cc: str):
    image = get_flag(cc)
    save_flag(image, f'{cc}.gif')
    print(cc, end=' ', flush=True)
    return cc

def download_many(cc_list: list[str]) -> int:
    """ Much slower with ProcessPoolExecutor because this specific task doesn't benefit from using processes and there
    is more overhead in creating processes than threads."""
    with futures.ThreadPoolExecutor() as executor:
    # with futures.ProcessPoolExecutor() as executor:
        res = executor.map(download_one, sorted(cc_list))
    return len(list(res))

if __name__ == '__main__':
    main(download_many)

"""
default: max_workers = min(32, os.cpu_count() + 4)

This default value preserves at least 5 workers for I/O bound tasks. It utilizes at most 32 CPU cores for CPU bound 
tasks which release the GIL. And it avoids using very large resources implicitly on many-core machines.
ThreadPoolExecutor now reuses idle worker threads before starting max_workers worker threads too.

Thread vs Process note:
Processes use more memory and take longer to start than threads, so the real value of ProcessPoolExecutor is in 
CPU-intensive jobs. 
"""