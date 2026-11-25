def pancake_sort(arr):

    limit = len(arr)

    while limit > 1:

        mi = arr.index(max(arr[:limit]))

        arr = arr[mi::-1] + arr[mi + 1:]

        arr = arr[limit - 1::-1] + arr[limit:]

        limit -= 1

    return arr

