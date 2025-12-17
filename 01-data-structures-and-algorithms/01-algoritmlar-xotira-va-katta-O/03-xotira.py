"""
03. Xotira - Amaliy misollar
"""

import copy
import sys


# 1. Stack vs Heap
def stack_vs_heap_demo():
    """Stack va Heap farqi"""
    # Stack
    x = 5           # int - stack
    y = 10.5        # float - stack
    
    # Heap
    numbers = [1, 2, 3, 4, 5]        # list - heap
    person = {"ism": "Ali", "yosh": 25}  # dict - heap
    
    print("Stack (oddiy o'zgaruvchilar):")
    print(f"  x = {x}, xotira: {sys.getsizeof(x)} bytes")
    print(f"  y = {y}, xotira: {sys.getsizeof(y)} bytes")
    
    print("\nHeap (murakkab ma'lumotlar):")
    print(f"  numbers = {numbers}, xotira: {sys.getsizeof(numbers)} bytes")
    print(f"  person = {person}, xotira: {sys.getsizeof(person)} bytes")


# 2. Pass by Value (Immutable)
def pass_by_value_demo():
    """Immutable o'zgaruvchilar - Pass by Value"""
    
    def ozgartir(x):
        print(f"    Funksiya ichida (avval): x = {x}")
        x = 100
        print(f"    Funksiya ichida (keyin): x = {x}")
    
    a = 5
    print(f"  Funksiya chaqirishdan avval: a = {a}")
    ozgartir(a)
    print(f"  Funksiya chaqirishdan keyin: a = {a} ← O'zgarmadi!")


# 3. Pass by Reference (Mutable)
def pass_by_reference_demo():
    """Mutable o'zgaruvchilar - Pass by Reference"""
    
    def ozgartir_list(lst):
        print(f"    Funksiya ichida (avval): {lst}")
        lst.append(100)
        print(f"    Funksiya ichida (keyin): {lst}")
    
    numbers = [1, 2, 3]
    print(f"  Funksiya chaqirishdan avval: {numbers}")
    ozgartir_list(numbers)
    print(f"  Funksiya chaqirishdan keyin: {numbers} ← O'zgardi!")


# 4. Shallow vs Deep Copy
def copy_demo():
    """Shallow va Deep Copy farqi"""
    
    # Original list
    original = [1, 2, [3, 4]]
    print(f"  Original: {original}")
    
    # Shallow Copy
    shallow = copy.copy(original)
    shallow[2][0] = 999
    print(f"\n  Shallow copy qilgandan keyin:")
    print(f"    Shallow: {shallow}")
    print(f"    Original: {original} ← O'zgardi! (Shallow copy)")
    
    # Deep Copy
    original2 = [1, 2, [3, 4]]
    deep = copy.deepcopy(original2)
    deep[2][0] = 999
    print(f"\n  Deep copy qilgandan keyin:")
    print(f"    Deep: {deep}")
    print(f"    Original: {original2} ← O'zgarmadi! (Deep copy)")


# 5. Xotira samaradorligi
def memory_efficiency_demo():
    """Xotira samarali ishlatish"""
    import time
    
    n = 10000
    
    # Yomon usul - har safar yangi list
    def yomon_usul(n):
        result = []
        for i in range(n):
            result = result + [i]  # Har safar yangi list!
        return result
    
    # Yaxshi usul - mavjud list'ga qo'shish
    def yaxshi_usul(n):
        result = []
        for i in range(n):
            result.append(i)  # O'sha list!
        return result
    
    # Yomon usul
    start = time.time()
    yomon_natija = yomon_usul(n)
    yomon_time = time.time() - start
    
    # Yaxshi usul
    start = time.time()
    yaxshi_natija = yaxshi_usul(n)
    yaxshi_time = time.time() - start
    
    print(f"  n = {n}")
    print(f"  Yomon usul:  {yomon_time:.4f}s")
    print(f"  Yaxshi usul: {yaxshi_time:.4f}s")
    print(f"  Yaxshi usul {yomon_time/yaxshi_time:.1f}x tezroq!")


# 6. O'zgaruvchilarning xotira hajmi
def memory_size_demo():
    """Turli ma'lumotlarning xotira hajmi"""
    
    data = {
        "int (1)": 1,
        "int (1000000)": 1000000,
        "float": 3.14,
        "str (qisqa)": "Hi",
        "str (uzun)": "A" * 100,
        "list (bo'sh)": [],
        "list (10 element)": list(range(10)),
        "dict (bo'sh)": {},
        "dict (10 element)": {i: i for i in range(10)},
        "set (bo'sh)": set(),
        "set (10 element)": set(range(10)),
    }
    
    print("  Ma'lumot turi               | Xotira hajmi")
    print("  " + "-" * 50)
    
    for name, value in data.items():
        size = sys.getsizeof(value)
        print(f"  {name:28} | {size:6} bytes")


# TESTLAR
if __name__ == "__main__":
    print("=" * 70)
    print("XOTIRA - AMALIY MISOLLAR")
    print("=" * 70)
    
    print("\n1.  Stack vs Heap:")
    print("-" * 70)
    stack_vs_heap_demo()
    
    print("\n\n2.  Pass by Value (Immutable):")
    print("-" * 70)
    pass_by_value_demo()
    
    print("\n\n3.  Pass by Reference (Mutable):")
    print("-" * 70)
    pass_by_reference_demo()
    
    print("\n\n4.  Shallow vs Deep Copy:")
    print("-" * 70)
    copy_demo()
    
    print("\n\n5.  Xotira samaradorligi:")
    print("-" * 70)
    memory_efficiency_demo()
    
    print("\n\n6.  Xotira hajmi taqqoslash:")
    print("-" * 70)
    memory_size_demo()
    
    print("\n" + "=" * 70)
    print(" Barcha misollar tugadi!")
    print("=" * 70)
    
    print("\n Muhim xulosa:")
    print("  - List.append() > List + [item]")
    print("  - Deep copy xavfsizroq")
    print("  - Immutable o'zgaruvchilar funksiyada o'zgarmaydi")
    print("  - Mutable o'zgaruvchilar funksiyada o'zgaradi")