import random
import time


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


# Sprawdzenie poniżej

random_numbers = generate_random_numbers(10)
print("Generated Numbers:", random_numbers)

start_time = time.time()
# sorted_numbers = sort_numbers(random_numbers)
# sorted_numbers = bubble_sort(random_numbers)
sorted_numbers = insertion_sort(random_numbers)
end_time = time.time()
print("Sorted Numbers (Bubble Sort):", sorted_numbers)

is_sorted = verify_sorted(sorted_numbers)
print("Are the numbers sorted?:", is_sorted)

print("Time taken by bubble_sort:", end_time - start_time, "s")
