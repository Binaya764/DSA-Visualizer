def Insertion_sort(arr):
    steps = []
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Highlight key
        steps.append(("key", i, j, arr.copy()))

        while j >= 0 and arr[j] > key:
            # Compare
            steps.append(("compare", j, j + 1, arr.copy()))

            arr[j + 1] = arr[j]  # shift
            steps.append(("shift", j, j + 1, arr.copy()))

            j -= 1

        arr[j + 1] = key
        steps.append(("insert", j + 1, i, arr.copy()))

    return steps
