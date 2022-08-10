def limit(arr, min_lim=None, max_lim=None):
    if not arr:
        return arr
    if min_lim is None:
        min_lim = min(arr)
    if max_lim is None:
        max_lim = max(arr)

    return list(filter(lambda x: (min_lim <= x <= max_lim), arr))
