# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass
# sorter.py
def insertion_sort_steps(arr):
    """
    Generates a list of steps for insertion sort.
    Each step is a tuple: (current_array, positions, highlight_indices)
    """
    steps = []
    n = len(arr)
    positions = list(range(n))

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            positions[j + 1] = positions[j]
            steps.append((arr[:], positions[:], [j, j + 1]))
            j -= 1
        arr[j + 1] = key
        positions[j + 1] = i
        steps.append((arr[:], positions[:], [j + 1]))
    return steps
