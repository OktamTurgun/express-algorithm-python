"""
04. Big O (Katta O) - Amaliy misollar va comparison
"""

import time
import random


# O(1) - Constant
def constant_time(arr):
    """
    O(1) - Doimiy vaqt
    Array hajmidan qat'iy nazar, bir xil vaqt
    """
    return arr[0] if arr else None


# O(log n) - Logarithmic
def binary_search(arr, target):
    """
    O(log n) - Logaritmik
    Har qadamda yarmi qoladi
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


# O(n) - Linear
def linear_search(arr, target):
    """
    O(n) - Chiziqli
    Har bir elementni tekshirish
    """
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


# O(n log n) - Linearithmic
def merge_sort(arr):
    """
    O(n log n) - Linearithmik
    Samarali sorting
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


def merge(left, right):
    """Ikkita sorted array'ni birlashtirish"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# O(n²) - Quadratic
def bubble_sort(arr):
    """
    O(n²) - Kvadratik
    Ichma-ich 2 ta loop
    """
    arr = arr.copy()
    n = len(arr)
    
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr


# O(2ⁿ) - Exponential
def fibonacci_slow(n):
    """
    O(2ⁿ) - Eksponensial
    Juda sekin - har safar 2 ta rekursiv chaqiruv
    """
    if n <= 1:
        return n
    return fibonacci_slow(n - 1) + fibonacci_slow(n - 2)


def fibonacci_fast(n):
    """
    O(n) - Chiziqli
    Tez - iterativ usul
    """
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# Performance Comparison
def compare_algorithms():
    """Turli algoritmlarning tezligini solishtirish"""
    
    sizes = [100, 1000, 10000]
    
    print("=" * 80)
    print("BIG O COMPARISON - PERFORMANCE TEST")
    print("=" * 80)
    
    for n in sizes:
        print(f"\n📊 n = {n:,}")
        print("-" * 80)
        
        # O(1) - Constant
        arr = list(range(n))
        start = time.time()
        for _ in range(100000):
            constant_time(arr)
        o1_time = time.time() - start
        print(f"O(1)       Constant      : {o1_time:.6f}s")
        
        # O(log n) - Binary Search
        arr_sorted = sorted(arr)
        start = time.time()
        for _ in range(10000):
            binary_search(arr_sorted, n // 2)
        olog_time = time.time() - start
        print(f"O(log n)   Logarithmic   : {olog_time:.6f}s")
        
        # O(n) - Linear Search
        start = time.time()
        for _ in range(1000):
            linear_search(arr, n // 2)
        on_time = time.time() - start
        print(f"O(n)       Linear        : {on_time:.6f}s")
        
        # O(n log n) - Merge Sort (faqat kichik n uchun)
        if n <= 1000:
            arr_random = [random.randint(1, 1000) for _ in range(n)]
            start = time.time()
            merge_sort(arr_random)
            onlogn_time = time.time() - start
            print(f"O(n log n) Linearithmic : {onlogn_time:.6f}s")
        
        # O(n²) - Bubble Sort (faqat juda kichik n uchun)
        if n <= 100:
            arr_random = [random.randint(1, 100) for _ in range(n)]
            start = time.time()
            bubble_sort(arr_random)
            on2_time = time.time() - start
            print(f"O(n²)      Quadratic     : {on2_time:.6f}s")


# Space Complexity Examples
def space_complexity_demo():
    """Xotira murakkabligi misollari"""
    
    print("\n\n" + "=" * 80)
    print("SPACE COMPLEXITY")
    print("=" * 80)
    
    # O(1) Space
    def sum_o1(arr):
        """O(1) space - faqat 1 ta o'zgaruvchi"""
        total = 0
        for num in arr:
            total += num
        return total
    
    # O(n) Space
    def copy_array(arr):
        """O(n) space - yangi array"""
        return arr.copy()
    
    # O(n) Space - Recursion
    def factorial_recursive(n):
        """O(n) space - call stack"""
        if n <= 1:
            return 1
        return n * factorial_recursive(n - 1)
    
    import sys
    
    n = 1000
    arr = list(range(n))
    
    print(f"\n📏 n = {n}")
    print("-" * 80)
    print(f"Original array size : {sys.getsizeof(arr):,} bytes")
    
    result1 = sum_o1(arr)
    print(f"sum_o1() result     : {sys.getsizeof(result1)} bytes - O(1) space")
    
    result2 = copy_array(arr)
    print(f"copy_array() result : {sys.getsizeof(result2):,} bytes - O(n) space")


# Big O Visualization
def visualize_big_o():
    """Big O ni vizualizatsiya qilish"""
    
    print("\n\n" + "=" * 80)
    print("BIG O VISUALIZATION")
    print("=" * 80)
    
    print("\n📈 n = 100 uchun operatsiyalar soni:")
    print("-" * 80)
    
    n = 100
    
    complexities = {
        "O(1)": 1,
        "O(log n)": int(n ** 0.5),  # taxminan log2(n)
        "O(n)": n,
        "O(n log n)": int(n * (n ** 0.5)),
        "O(n²)": n * n,
    }
    
    max_ops = max(complexities.values())
    
    for name, ops in complexities.items():
        bar_length = int((ops / max_ops) * 50)
        bar = "█" * bar_length
        print(f"{name:12} : {bar} {ops:,}")
    
    print("\n⚠️  O(2ⁿ) va O(n!) juda katta - ko'rsatib bo'lmaydi!")


# Common Operations Big O
def common_operations():
    """Keng tarqalgan operatsiyalarning Big O"""
    
    print("\n\n" + "=" * 80)
    print("PYTHON DATA STRUCTURES - BIG O")
    print("=" * 80)
    
    operations = {
        "List": [
            ("arr[i]", "O(1)"),
            ("arr.append(x)", "O(1)"),
            ("arr.insert(0, x)", "O(n)"),
            ("arr.pop()", "O(1)"),
            ("arr.pop(0)", "O(n)"),
            ("x in arr", "O(n)"),
            ("arr.sort()", "O(n log n)"),
        ],
        "Dict": [
            ("dict[key]", "O(1)"),
            ("dict[key] = val", "O(1)"),
            ("del dict[key]", "O(1)"),
            ("key in dict", "O(1)"),
        ],
        "Set": [
            ("x in set", "O(1)"),
            ("set.add(x)", "O(1)"),
            ("set.remove(x)", "O(1)"),
        ],
    }
    
    for data_structure, ops in operations.items():
        print(f"\n{data_structure}:")
        print("-" * 80)
        for op, complexity in ops:
            print(f"  {op:25} → {complexity}")


# TESTLAR
if __name__ == "__main__":
    print("=" * 80)
    print("BIG O (KATTA O) - AMALIY MISOLLAR")
    print("=" * 80)
    
    # 1. Fibonacci comparison
    print("\n1  Fibonacci: O(2ⁿ) vs O(n)")
    print("-" * 80)
    
    n = 30
    print(f"Fibonacci({n}) ni hisoblash:\n")
    
    start = time.time()
    result = fibonacci_fast(n)
    fast_time = time.time() - start
    print(f"O(n) - Tez usul  : {result} ({fast_time:.6f}s)")
    
    start = time.time()
    result = fibonacci_slow(n)
    slow_time = time.time() - start
    print(f"O(2ⁿ) - Sekin usul: {result} ({slow_time:.6f}s)")
    
    print(f"\n⚡ Tez usul {slow_time/fast_time:.0f}x tezroq!")
    
    # 2. Algorithm comparison
    compare_algorithms()
    
    # 3. Space complexity
    space_complexity_demo()
    
    # 4. Visualization
    visualize_big_o()
    
    # 5. Common operations
    common_operations()
    
    print("\n\n" + "=" * 80)
    print(" BIG O AMALIY MISOLLAR TUGADI!")
    print("=" * 80)
    
    print("\n XULOSA:")
    print("  • O(1) > O(log n) > O(n) > O(n log n) > O(n²) > O(2ⁿ) > O(n!)")
    print("  • Konstantalarni e'tiborsiz qoldiramiz: O(2n) = O(n)")
    print("  • Eng katta hadni olamiz: O(n² + n) = O(n²)")
    print("  • Time va Space Complexity ikkalasi ham muhim!")