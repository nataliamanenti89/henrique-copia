def tournament_sort(arr): 
    if len(arr) <= 1: 
        return arr.copy() 

    elements = arr.copy()
    n = len(elements)

    index = 1
    while index < n:
        index *= 2
    tree = [None] * (2 * index) 

    for i in range(n):
        tree[index + i] = i

    def winner(a, b):

        if a is None: 
            return b 

        if b is None: 
            return a

        if elements[a] <= elements[b]:
            return a 

        return b 

    for i in range(index - 1, 0, -1):
        tree[i] = winner(
            tree[2 * i],
            tree[2 * i + 1]
        )

    results = []

    for _ in range(n): 

        indicator = tree[1] 

        results.append(elements[indicator])

        position = index + indicator

        tree[position] = None

        position //=2

        while position >= 1:

            tree[position] = winner(
                tree[2 * position],
                tree[2 * position + 1]
            )

            position //=2

    return results
