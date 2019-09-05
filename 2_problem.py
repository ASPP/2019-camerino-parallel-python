def myreduce(func, inplist):
    """A parallelizable reduce function"""
    # ***YOUR CODE HERE***
    while len(inplist) > 1:
        
        output = []
        
        for pair in list(zip(inplist[::2], inplist[1::2])):
            output.append(func(pair[0],pair[1]))

        if len(inplist) % 2 != 0: 
            output.append(inplist[-1])

        inplist = output

    return output
