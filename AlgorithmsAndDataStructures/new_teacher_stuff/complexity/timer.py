import functools
import time


def time_execution(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        delta = time.time() - start
        print(f"Executing {f.__name__} took {delta: .7f}s. ")
        return result
    return wrapper
