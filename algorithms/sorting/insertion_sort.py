# algorithms/insertion_sort.py

def insertion_sort_steps(arr):
    """
    Insertion sort logic that generates step-by-step states for visualization.
    Each step contains:
        - 'array': current array state
        - 'highlight': indices being compared or moved
        - 'key': index of current key element
    """
    array = arr.copy()
    steps = []
    steps.append({"array": array.copy(), "highlight": {}, "key": None})  # Initial state

    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        steps.append({
            "array": array.copy(),
            "highlight": {i: True},  # Key element
            "key": i
        })

        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            steps.append({
                "array": array.copy(),
                "highlight": {j: True, j+1: True},  # Comparing/swapping
                "key": i
            })
            j -= 1

        array[j + 1] = key
        steps.append({
            "array": array.copy(),
            "highlight": {j+1: True},  # Key inserted
            "key": j+1
        })

    return steps
