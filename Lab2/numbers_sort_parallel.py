import random
import time
from multiprocessing import Pool


def generate_random_numbers(n, lower_bound=0, upper_bound=100):
    return [random.randint(lower_bound, upper_bound) for _ in range(n)]

def sort_numbers(numbers):
    #Using Python's builtin function
    return sorted(numbers)

def verify_sorted(numbers):
    return all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))

def bubble_sort(numbers):
    sorted_numbers = numbers[:]  # Create a copy

    n = len(sorted_numbers)

    for i in range(n):

        for j in range(0, n - i - 1):

            if sorted_numbers[j] > sorted_numbers[j + 1]:

                # Swap if the element found is greater than the next element

                sorted_numbers[j], sorted_numbers[j + 1] = sorted_numbers[j + 1], sorted_numbers[j]

    return sorted_numbers


def insertion_sort(numbers):
    sorted_numbers = numbers[:]  # Create a copy
    for i in range(1, len(sorted_numbers)):
        key = sorted_numbers[i]
        j = i - 1
        # Move elements of sorted_numbers[0..i-1], that are greater than key,
        # one position ahead of their current position
        while j >= 0 and sorted_numbers[j] > key:
            sorted_numbers[j + 1] = sorted_numbers[j]
            j -= 1
        sorted_numbers[j + 1] = key
    return sorted_numbers

def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    mid = len(numbers) // 2
    left = merge_sort(numbers[:mid])
    right = merge_sort(numbers[mid:])
    return merge(left, right)

def merge(left, right):
    sorted_list = []
    while left and right:
        if left[0] <= right[0]:
            sorted_list.append(left.pop(0))
        else:
            sorted_list.append(right.pop(0))
    sorted_list.extend(left)
    sorted_list.extend(right)
    return sorted_list

def parallel_merge_sort(numbers, pool_size=4):
    if len(numbers) <= 1:
        return numbers

    pool = Pool(processes=pool_size)
    size = len(numbers) // pool_size
    sublists = [numbers[i * size:(i + 1) * size] for i in range(pool_size)]
    sublists[-1].extend(numbers[pool_size * size:])  # Include remaining elements in the last sublist

    sorted_sublists = pool.map(merge_sort, sublists)

    while len(sorted_sublists) > 1:
        extra = sorted_sublists.pop() if len(sorted_sublists) % 2 == 1 else None
        sorted_sublists = [merge(sorted_sublists[i], sorted_sublists[i + 1]) for i in range(0, len(sorted_sublists) - 1, 2)]
        if extra:
            sorted_sublists.append(extra)

    pool.close()
    pool.join()
    return sorted_sublists[0] if sorted_sublists else extra

# Sprawdzenie poniżej
if __name__ == '__main__': #inaczej te funkcje były by wywoływane nawet w unit testach
    random_numbers = generate_random_numbers(10)
    print("Generated Numbers:", random_numbers)

    start_time = time.time()
    # sorted_numbers = sort_numbers(random_numbers)
    # sorted_numbers = bubble_sort(random_numbers)
    # sorted_numbers = insertion_sort(random_numbers)
    sorted_numbers = parallel_merge_sort(random_numbers, 4)
    end_time = time.time()
    print("Sorted Numbers:", sorted_numbers)

    is_sorted = verify_sorted(sorted_numbers)
    print("Are the numbers sorted?:", is_sorted)
    print("Is the result the same as builtin function?", sorted_numbers == sort_numbers(random_numbers))

    print("Time taken by:", end_time - start_time, "s")
