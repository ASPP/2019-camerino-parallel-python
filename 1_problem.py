from time import time

def func(i):
    """A dummy CPU-bound function."""
    print(f'Function {i} starting...')
    start = time()
    # ***INSERT CODE HERE*** (should take about 1 second to execute)
    random_array = np.random.rand(5001000)
    aux = []
    for k in random_array:
        if k > 0.5:
            aux.append(k)
        else:
            aux.append(0)
    print(time()-start)
    print(f'Function {i} done')
    return i

lazy = [delayed(func)(i) for i in range(4)]  # DON'T CHANGE (explained later)
