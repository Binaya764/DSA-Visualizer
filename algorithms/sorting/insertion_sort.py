def Insertion_sort(arr):
    steps = []
    n = len(arr)


    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Highlight key include key value for visualization
        steps.append(("key", i, j, arr.copy(), key))

        while j >= 0 and arr[j] > key:
            # Compare
            steps.append(("compare", j, j + 1, arr.copy()))

            # Shift element right
            arr[j + 1] = arr[j]
            steps.append(("shift", j, j+1 , arr.copy(), key))

            j -= 1

        # Insert key at correct position
        arr[j + 1] = key
        steps.append(("insert", j + 1, i, arr.copy(), key))

    return steps
