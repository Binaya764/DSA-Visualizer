def selection_sort(arr):
    """
    Performs selection sort and returns steps for visualization.
    Each step is a tuple: ('compare'/'swap', i, j, current_array_state)
    """
    steps = []
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            steps.append(("compare", min_idx, j, arr.copy()))
            if arr[j] < arr[min_idx]:
                min_idx = j

        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            steps.append(("swap", i, min_idx, arr.copy()))

    return steps
