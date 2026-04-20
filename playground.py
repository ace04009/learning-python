arrivals=['Paul', 'John', 'Ringo', 'George']

def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    ind = arrivals.index(name) 
    if ((ind > (len(arrivals)/2)) and arrivals[ind] != arrivals[-1]):
        return True
    return False

print(fashionably_late(arrivals, 'Ringo')) # True

help(str)