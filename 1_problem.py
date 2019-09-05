from dask import delayed  # DON'T CHANGE (explained later)
import numpy as np

def func(i):
    """A dummy CPU-bound function."""
    print(f'Function {i} starting...')
    # ***INSERT CODE HERE*** (should take about 1 second to execute)
    np.random.rand(int(1e8))
    print(f'Function {i} done')
    return i

lazy = [delayed(func)(i) for i in range(4)]  # DON'T CHANGE (explained later)
