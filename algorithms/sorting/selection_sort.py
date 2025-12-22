def selection_sort(arr):
    steps = []
    a = arr.copy()
    n = len(a)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            steps.append(("compare", min_index, j, a.copy()))
            if a[j] < a[min_index]:
                min_index = j
                steps.append(("select_min", min_index, j, a.copy()))
            if min_index != i: a[i], a[min_index] = a[min_index], a[i]
            steps.append(("swap", i, min_index, a.copy()))
    return steps# This Python file uses the following encoding: utf-8


