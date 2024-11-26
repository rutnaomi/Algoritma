import random

random.seed(42)

data = [random.randint(0, 100) for _ in range(50)]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

sorted_data = bubble_sort(data)

print("Data awal:", data)
print("Data setelah sorting (Naive Sort):", sorted_data)
