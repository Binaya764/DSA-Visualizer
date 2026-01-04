def binary_search(arr, target):
    steps = []
    left, right = 0, len(arr) - 1


    steps.append(("initial", left, (left+right)//2, right, arr.copy(), left, right))

    while left <= right:
        mid = (left + right) // 2

        # Step: checking current mid
        steps.append(("check", left, mid, right, arr[left:right+1].copy(), left, right))

        if arr[mid] == target:
            # Step: found
            steps.append(("found", left, mid, right, arr[left:right+1].copy(), left, right))
            return steps
        elif arr[mid] < target:
            # Going high - next iteration will use right half
            old_left = left
            old_mid = mid
            old_right = right
            left = mid + 1
            if left <= right:
                new_sub_arr = arr[left:right+1].copy()
            else:
                new_sub_arr = []
            steps.append(("high", old_left, old_mid, old_right, new_sub_arr, left, right))
        else:
            # Going low - next iteration will use left half
            old_left = left
            old_mid = mid
            old_right = right
            right = mid - 1
            if left <= right:
                new_sub_arr = arr[left:right+1].copy()
            else:
                new_sub_arr = []
            steps.append(("low", old_left, old_mid, old_right, new_sub_arr, left, right))

    # Step: not found
    steps.append(("not_found", left, -1, right, [], left, right))
    return steps
