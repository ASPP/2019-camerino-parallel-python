from dask import delayed  # DON'T CHANGE (explained later)
import numpy as np

def func(i):
    """A dummy CPU-bound function."""
    print(f'Function {i} starting...')
    A = np.random.rand(750,750)
    np.sum(np.linalg.eigvals(A))
    print(f'Function {i} done')

    return i

lazy = [delayed(func)(i) for i in range(4)]  # DON'T CHANGE (explained later)
