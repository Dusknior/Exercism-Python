def flatten(iterable):
    flat_list = []
    for item in iterable:
        if isinstance(item, (list, tuple)):
            item = flatten(item)
            flat_list.extend(subitem for subitem in item)
        elif item is not None:
            flat_list.append(item)
    return flat_list
