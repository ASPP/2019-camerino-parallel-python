from dask import delayed  # DON'T CHANGE (explained later)

def func(i):
    """A dummy CPU-bound function."""
    print(f'Function {i} starting...')
    # ***INSERT CODE HERE*** (should take about 1 second to execute)
    sum = 0
    for j in range(5000000):
        sum = sum+j
    print(sum)

    print(f'Function {i} done')
    return i

lazy = [delayed(func(i)) for i in range(4)]  # DON'T CHANGE (explained later)
