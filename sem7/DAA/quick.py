import random
import time

def deterministic_partition(arr, low, high):
    # Select the middle element as the pivot
    pivot = arr[(low + high) // 2]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # Swap arr[i] and arr[j]
        arr[i], arr[j] = arr[j], arr[i]

def deterministic_quicksort(arr, low, high):
    if low < high:
        # Partition the array into two subarrays
        partition_index = deterministic_partition(arr, low, high)

        # Recursively sort the subarrays
        deterministic_quicksort(arr, low, partition_index)
        deterministic_quicksort(arr, partition_index + 1, high)

def randomized_partition(arr, low, high):
    # Select a random pivot
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_quicksort(arr, low, high):
    if low < high:
        partition_index = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, partition_index - 1)
        randomized_quicksort(arr, partition_index + 1, high)

if __name__ == "__main__":
    # n = 1000  # Change the size of the input array as needed
    # arr = [random.randint(1, n) for _ in range(n)]
    arr = [23,45,67,89,34,34,89]

    n = len(arr)

    # Analyze deterministic quicksort
    start_time = time.time()
    deterministic_quicksort(arr, 0, n - 1)
    deterministic_time = time.time() - start_time
    print("Deterministic = ", arr)

    arr1 = [23,45,67,89,34,34,89]

    n = len(arr1)

    # Analyze randomized quicksort
    start_time = time.time()
    randomized_quicksort(arr1, 0, n - 1)
    randomized_time = time.time() - start_time
    print("Randomized = ", arr1)

    print(f"Deterministic Quicksort Time: {deterministic_time:.6f} seconds")
    print(f"Randomized Quicksort Time: {randomized_time:.6f} seconds")
