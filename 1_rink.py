from dask import delayed  # DON'T CHANGE (explained later)

def func(i):
    """A dummy CPU-bound function."""
    print(f'Function {i} starting...')
    n = 2e7
    while n > 0:
        n -= 1
    print(f'Function {i} done')
    return i

lazy = [delayed(func)(i) for i in range(4)]  # DON'T CHANGE (explained later)