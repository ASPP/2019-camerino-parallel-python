def myreduce(f, inputs):
    """A parallelizable reduce function"""

    while(True):
        n = len(inputs)
        if n == 1:
            return inputs[0]
        else:
            inputs = ([f(inputs[i], inputs[n//2 + i])  # divide & conquer
                       for i in range(n//2)] +
                       list(inputs[n // 2 * 2:]))      # take care of uneven list here
