from dask import delayed  # DON'T CHANGE (explained later)

def func(i):
    """A dummy CPU-bound function."""
    print(f'Function {i} starting...')
    fakeList = []
    for i in range(10000):
        fakeList.append(i)
    # ***INSERT CODE HERE*** (should take about 1 second to execute)
    print(f'Function {i} done')
    return i

lazy = [delayed(func)(i) for i in range(4)]  # DON'T CHANGE (explained later)
