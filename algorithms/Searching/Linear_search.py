def linear_search(arr, target):
    steps = []

    for i in range(len(arr)):
        steps.append(("check", i,arr.copy()))


        if arr[i] == target:
            steps.append(("found",i,arr.copy()))
            return steps, True  # found

    steps.append(("not found",-1,arr.copy()))

    return steps, False  # not found
""" step = {
     "index": i,
     "value": arr[i],
     "is_match": arr[i] == target
 }
 steps.append(step)"""
