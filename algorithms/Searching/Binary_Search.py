def binary_search(arr, target):
    steps = []
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # Step: checking current mid
        steps.append(("check", mid, arr.copy()))

        if arr[mid] == target:
            # Step: found
            steps.append(("found", mid, arr.copy()))
            return steps

        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # Step: not found
    steps.append(("not_found", -1, arr.copy()))
    return steps
