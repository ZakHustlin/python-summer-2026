def flatten(iterable):
    newlist = []
    for item in iterable:
        if isinstance(item, list) is True:
            newlist.extend(flatten(item))
        elif item == None:
            iterable.remove(item)
        else:
            newlist.append(item)

    return newlist
