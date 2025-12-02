def linear_search_steps(arr, target):
    steps = []

    for i in range(len(arr)):
        step = {
            "index": i,
            "value": arr[i],
            "is_match": arr[i] == target
        }
        steps.append(step)

        if arr[i] == target:
            return steps, True  # found

    return steps, False  # not found
