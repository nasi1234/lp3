import random
import time


def quick_sort_deterministic(arr):
    if len(arr) <= 1:
        return arr
    pivot   = arr[-1] 
    left    = [x for x in arr[:-1] if x <= pivot]
    right   = [x for x in arr[:-1] if x >  pivot]
    return quick_sort_deterministic(left) + [pivot] + quick_sort_deterministic(right)

def quick_sort_randomized(arr):
    if len(arr) <= 1:
        return arr
    pivot   = arr[random.randint(0, len(arr) - 1)] 
    left    = [x for x in arr if x <  pivot]
    middle  = [x for x in arr if x == pivot]
    right   = [x for x in arr if x >  pivot]
    return quick_sort_randomized(left) + middle + quick_sort_randomized(right)

def analyze_sorting():

    n = int(input("Enter number of elements: "))
    arr = [random.randint(1, 1000) for _ in range(n)] 
    print("Original array:", arr)
    

    start = time.time()
    s_a_d = quick_sort_deterministic(arr.copy())
    end   = time.time()
    t_d   = end - start
    print("\nDeterministic QuickSort result:", s_a_d)
    print(f"Time taken by Deterministic QuickSort: {t_d:.6f} seconds")
    

    start = time.time()
    s_a_r = quick_sort_randomized(arr.copy())
    end   = time.time()
    t_r   = end - start
    print("\nRandomized QuickSort result:", s_a_r)
    print(f"Time taken by Randomized QuickSort: {t_r:.6f} seconds")

analyze_sorting()
