def reverse_sort_dictionary(d):
    return sorted([(k, v[0]) for k, v in d.items()], reverse=True)