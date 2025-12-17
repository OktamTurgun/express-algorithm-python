# Big O (Katta O) Notation

## Big O nima?

**Big O** - bu algoritmning ishlash vaqti yoki xotira sarfini baholash usuli.

## Nega kerak?

-  Algoritmlarni solishtirish
-  Samaradorlikni bashorat qilish
-  Bottleneck (to'siq) topish
-  Interview'da kerak bo'ladi!

## Time Complexity (Vaqt murakkabligi)

### O(1) - Constant (Doimiy)

Kiruvchi hajmidan qat'iy nazar, har doim bir xil vaqt.
```python
def birinchi_element(arr):
    return arr[0]  # O(1)

def ikki_elementni_almashir(a, b):
    return b, a    # O(1)
```

**Grafik**: `━━━━` (Tekis chiziq)

---

### O(log n) - Logarithmic

Har qadamda ma'lumotning yarmi qoladi.
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Topilmadi

# O(log n) - Juda tez!
```

**Misol**: 1,000,000 elementda ~20 qadam

**Grafik**: `━━━╱` (Sekin o'sadi)

---

### O(n) - Linear

Har bir element uchun 1 marta.
```python
def eng_katta(arr):
    maksimum = arr[0]
    for son in arr:      # O(n)
        if son > maksimum:
            maksimum = son
    return maksimum

def yigindi(arr):
    jami = 0
    for son in arr:      # O(n)
        jami += son
    return jami
```

**Grafik**: `━━╱╱╱` (To'g'ri chiziq)

---

### O(n log n) - Linearithmic

Eng yaxshi sorting algoritmlar.
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

# O(n log n) - Samarali sorting
```

**Misol**: QuickSort, MergeSort, HeapSort

**Grafik**: `━━╱╱╱╱` (n dan biroz tezroq o'sadi)

---

### O(n²) - Quadratic

Ichma-ich 2 ta loop.
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):           # O(n)
        for j in range(n - i - 1):  # O(n)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# O(n²) - Sekin!
```

**Misol**: 1000 element = 1,000,000 operatsiya!

**Grafik**: `━╱╱╱╱╱` (Tez o'sadi)

---

### O(2ⁿ) - Exponential

Har qadam uchun 2 barobar ko'payadi.
```python
def fibonacci_rekursiv(n):
    if n <= 1:
        return n
    return fibonacci_rekursiv(n - 1) + fibonacci_rekursiv(n - 2)

# O(2ⁿ) - Juda sekin! 
```

**Misol**: n=30 uchun ~1,000,000,000 chaqiruv!

**Grafik**: `╱╱╱╱╱╱` (Juda tez o'sadi)

---

### O(n!) - Factorial

Eng sekin! Barcha permutatsiyalar.
```python
def permutations(arr):
    if len(arr) <= 1:
        return [arr]
    
    result = []
    for i in range(len(arr)):
        rest = arr[:i] + arr[i+1:]
        for p in permutations(rest):
            result.append([arr[i]] + p)
    
    return result

# O(n!) - Faqat kichik n uchun!
```

**Misol**: n=10 uchun 3,628,800 permutatsiya!

---

## Big O Solishtirish
```
Tez ←                                                    → Sekin
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)
```

### n = 100 uchun:

| Big O      | Operatsiyalar | Taxminiy vaqt |
|------------|---------------|---------------|
| O(1)       | 1             | 1 nanosekund  |
| O(log n)   | ~7            | 7 nanosekund  |
| O(n)       | 100           | 100 nanosekund|
| O(n log n) | ~700          | 700 nanosekund|
| O(n²)      | 10,000        | 10 mikrosekund|
| O(2ⁿ)      | 1.26×10³⁰     | ∞ (imkonsiz!) |
| O(n!)      | 9.33×10¹⁵⁷    | ∞ (imkonsiz!) |

---

## Space Complexity (Xotira murakkabligi)

### O(1) - Constant Space
```python
def yigindi(arr):
    jami = 0  # Faqat 1 ta o'zgaruvchi
    for son in arr:
        jami += son
    return jami  # O(1) space
```

### O(n) - Linear Space
```python
def nusxa(arr):
    yangi = []
    for son in arr:
        yangi.append(son)
    return yangi  # O(n) space - yangi array
```

### O(n) - Rekursiya
```python
def faktorial(n):
    if n <= 1:
        return 1
    return n * faktorial(n - 1)
    # O(n) space - call stack'da n ta funksiya
```

---

## Qoidalar

### 1. Konstantalarni e'tiborsiz qoldiring
```python
# O(2n) = O(n)
# O(n/2) = O(n)
# O(100) = O(1)
```

### 2. Eng katta hadni oling
```python
# O(n² + n) = O(n²)
# O(n + log n) = O(n)
# O(n! + 2ⁿ) = O(n!)
```

### 3. Turli o'zgaruvchilar
```python
def ikki_array(arr1, arr2):
    for x in arr1:        # O(n)
        for y in arr2:    # O(m)
            print(x, y)
    # O(n * m) - ikkalasi turli!
```

---

## Amaliy Misollar

### Misol 1: Bir nechta loop
```python
def misol(arr):
    # Loop 1
    for x in arr:         # O(n)
        print(x)
    
    # Loop 2
    for x in arr:         # O(n)
        print(x)
    
    # Jami: O(n) + O(n) = O(2n) = O(n)
```

### Misol 2: Ichma-ich loop
```python
def misol(arr):
    for i in range(len(arr)):      # O(n)
        for j in range(len(arr)):  # O(n)
            print(arr[i], arr[j])
    
    # Jami: O(n) * O(n) = O(n²)
```

### Misol 3: Aralash
```python
def misol(arr):
    # Part 1
    for x in arr:              # O(n)
        print(x)
    
    # Part 2
    for i in range(len(arr)):       # O(n)
        for j in range(len(arr)):   # O(n)
            print(arr[i], arr[j])
    
    # Jami: O(n) + O(n²) = O(n²)
    # Chunki n² > n
```

---

## Best, Average, Worst Case

### QuickSort misoli:
- **Best Case**: O(n log n) - har doim o'rtani tanladik
- **Average Case**: O(n log n) - odatda
- **Worst Case**: O(n²) - eng yomon holda

Odatda **Worst Case** haqida gapiramiz!

---

## Xulosa

-  Big O - algoritm samaradorligini o'lchaydi
-  Time va Space Complexity
-  O(1) eng yaxshi, O(n!) eng yomon
-  Konstantalarni va kichik hadlarni e'tiborsiz qoldiring
-  Interview'da juda muhim!

---

## Cheat Sheet
```python
O(1)       - Array index, dict key lookup
O(log n)   - Binary search, balanced tree
O(n)       - Simple loop, linear search
O(n log n) - Merge sort, quick sort, heap sort
O(n²)      - Bubble sort, selection sort, nested loops
O(2ⁿ)      - Recursive fibonacci
O(n!)      - Permutations
```

---

## Amaliyot uchun savollar

1. `arr.append(x)` - qanday Big O?
2. `arr.insert(0, x)` - qanday Big O?
3. `arr.pop()` - qanday Big O?
4. `arr.pop(0)` - qanday Big O?
5. `x in arr` - qanday Big O?

**Javoblar**: O(1), O(n), O(1), O(n), O(n)