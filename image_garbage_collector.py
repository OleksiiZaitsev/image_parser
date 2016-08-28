import os

path = r'images/'

# CREATED DICT OF FILES IN DIR "{NAME:SIZE}"
def create_dict(path):
    unique = {}
    files = os.listdir(path)
    for i in files:
        unique['{}'.format(i)] = os.path.getsize(path + i)
    return unique


# CLEAN FILES FROM THE DICT WITH SAME SIZE
def search_for_clean(ls, prefix):
    garbage = []
    for i in ls.items():
        if i[1] == prefix:
            garbage.append(i[0])
    return garbage[1:]

def garbage_collector():
    items = create_dict(path).items()

    for i in items:
        for i in search_for_clean(create_dict(path), i[1]):
            os.remove(path + i)


