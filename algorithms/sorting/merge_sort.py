
def merge_Sort(arr):
    """
    Performs merge sort and returns steps for visualization.
    Each step is a tuple: ('compare'/'overwrite', i, j, current_array_state)
    """
    steps = []

    def merge(left, mid, right):
        L = arr[left:mid + 1]
        R = arr[mid + 1:right + 1]
        i = j = 0
        k = left

        while i < len(L) and j < len(R):
            steps.append(("compare", left + i, mid + 1 + j, arr.copy()))
            if L[i] <= R[j]:
                arr[k] = L[i]
                steps.append(("overwrite", k, left + i, arr.copy()))
                i += 1
            else:
                arr[k] = R[j]
                steps.append(("overwrite", k, mid + 1 + j, arr.copy()))
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            steps.append(("overwrite", k, left + i, arr.copy()))
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            steps.append(("overwrite", k, mid + 1 + j, arr.copy()))
            j += 1
            k += 1

    def merge_sort_recursive(left, right):
        if left < right:
            mid = (left + right) // 2
            merge_sort_recursive(left, mid)
            merge_sort_recursive(mid + 1, right)
            merge(left, mid, right)

    merge_sort_recursive(0, len(arr) - 1)
    return steps
