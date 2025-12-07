# algorithms/searching/binary_search.py
def binary_search(arr, target):
    steps = []
    a = sorted(arr)       # binary search operates on sorted array
    lo, hi = 0, len(a)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        steps.append(("check", mid, -1, a.copy()))
        if a[mid] == target:
            steps.append(("found", mid, -1, a.copy()))
            break
        elif a[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    steps.append(("done", -1, -1, a.copy()))
    return steps
