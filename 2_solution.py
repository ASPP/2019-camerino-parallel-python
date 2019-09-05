def myreduce(func, inplist):
    """A parallelizable reduce function"""
    if len(inplist) == 1:  # if one item, return it
        return inplist[0]
    elif len(inplist) == 2:  # if two items, call the function
        return func(*inplist)
    else:
        res_first = myreduce(func, inplist[:len(inplist) //2])  # recur reduce on first half
        res_second = myreduce(func, inplist[len(inplist) //2:])  # recur reduce on second half
        return func(res_first, res_second)
 