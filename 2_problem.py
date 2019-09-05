def myreduce(func, inplist):
    """A parallelizable reduce function"""
    output = inplist
    while len(output) !=1:
        aux=[]
        for (j,k) in zip(output[:-1],output[1:]):
            aux.append(func(j,k))
        output = aux
    return output 
