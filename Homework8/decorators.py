from time import time, sleep


def warn_slow(func):
    def wrapper(*args, **kwargs):
        start = time()
        res = func(*args, **kwargs)
        duration = time() - start
        if duration >= 2:
            print(f"execution of {func.__name__} with arguments {args} took more than 2 seconds ({duration})")
            print(f"execution of {func.__name__} with arguments {kwargs} took more than 2 seconds ({duration})")
        return res
    return wrapper

@warn_slow
def func_slow(a, b):
    sleep(2)
    print(a, b)

@warn_slow
def func_fast(a, b):
    print(a, b)


print(func_fast(5, 3))
print(func_slow(4, 6))
