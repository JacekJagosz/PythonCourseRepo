import unittest
from multiprocessing import cpu_count
import random
import time
import matplotlib.pyplot as plt
from numbers_sort_parallel import parallel_merge_sort

class TestParallelMergeSort(unittest.TestCase):
    def test_sort(self):
        data_sizes = [10, 100, 1000, 10000]
        num_processes = [1, 2, 4, cpu_count()]
        results = []

        for size in data_sizes:
            for processes in num_processes:
                with self.subTest(size=size, processes=processes):
                    numbers = [random.randint(0, 100) for _ in range(size)]
                    start_time = time.time()
                    sorted_numbers = parallel_merge_sort(numbers, pool_size=processes)
                    end_time = time.time()

                    self.assertEqual(sorted_numbers, sorted(numbers))
                    results.append({
                        'size': size,
                        'processes': processes,
                        'time': end_time - start_time
                    })

        # Plotting results
        plt.figure(figsize=(10, 6))
        for size in data_sizes:
            times = [result['time'] for result in results if result['size'] == size]
            plt.plot(num_processes, times, marker='o', label=f'Data Size: {size}')

        plt.xlabel('Number of Processes')
        plt.ylabel('Time (seconds)')
        plt.title('Parallel Merge Sort Performance')
        plt.legend()
        plt.grid(True)
        plt.show()

if __name__ == '__main__':
    unittest.main()
