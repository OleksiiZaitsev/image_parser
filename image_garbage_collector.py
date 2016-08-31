import os

# CREATED DICT OF FILES IN DIR "{NAME:SIZE}"
def ls(path):
    """RETURN DICT OF FILES {NAME:SIZE}"""
    items = {}
    files = os.listdir(path)
    for i in files:
        items['{}'.format(i)] = os.path.getsize(path + i)
    return items

# SEARCH FILES FROM THE DICT WITH SAME SIZE
def search_for_clean(ls, size):
    """RETURN LIST OF NAMES FOR DELETE"""
    garbage = []
    for i in ls.items():
        if i[1] == size:
            garbage.append(i[0])
    return garbage[1:]

# CLEAN FILES FROM THE DICT WITH SAME SIZE
def garbage_collector(path):

    items = ls(path)

    for size in items.values():

        for i in search_for_clean(items, size):
            if os.path.exists(path + i):
                print('# CLEAN FILES FROM THE DIR WITH SAME SIZE :', path + i)
                os.remove(path + i)
            else:
                pass
