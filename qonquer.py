import random

random.seed(42)

data = [random.randint(0, 100) for _ in range(50)]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

sorted_data = quick_sort(data)

print("Data awal:", data)
print("Data setelah sorting (Divide and Conquer):", sorted_data)
