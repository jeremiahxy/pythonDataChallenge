def filterLists(full_list, excludes):
    s = set(excludes)
    return (x for x in full_list if x not in s)