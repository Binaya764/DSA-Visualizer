def bubble_sort(arr):
    steps = []
    a = arr.copy()
    n = len(a)

    for i in range(n):
        for j in range(0, n - i - 1):
            steps.append(("compare", j, j + 1, a.copy()))

            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                steps.append(("swap", j, j + 1, a.copy()))

    return steps
