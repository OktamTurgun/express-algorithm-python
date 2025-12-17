# Xotira (Memory)

## Xotira nima?

**Xotira** - bu kompyuterda ma'lumotlarni vaqtinchalik yoki doimiy saqlash joyi.

## Xotira turlari

### 1. RAM (Random Access Memory)
- **Tez** - o'qish va yozish juda tez
- **Vaqtinchalik** - kompyuter o'chirilsa, ma'lumot yo'qoladi
- **Qimmat** - narxi yuqori

### 2. Disk (Hard Drive/SSD)
- **Sekin** - RAM'ga qaraganda sekinroq
- **Doimiy** - ma'lumot saqlanadi
- **Arzon** - narxi past

## Stack vs Heap

Python'da xotira 2 ta asosiy qismga bo'linadi:

### Stack (To'plam)
- **Tez** - juda tezkor
- **Cheklangan** - o'lchami kichik
- **Avtomatik** - o'zi boshqariladi
- **LIFO** - Last In First Out

**Nimalar stack'da?**
- Oddiy o'zgaruvchilar (int, float, bool)
- Funksiya chaqiruvlari
- Local o'zgaruvchilar
```python
# Stack'da
x = 5          # int - stack
y = 10.5       # float - stack
name = "Ali"   # str reference - stack, lekin qiymat heap'da

def salom():   # Funksiya chaqiruvi - stack
    a = 100    # Local o'zgaruvchi - stack
```

### Heap (Uyum)
- **Sekinroq** - stack'ga nisbatan
- **Katta** - o'lchami katta
- **Qo'lda boshqarish** - Python'da avtomatik (Garbage Collection)

**Nimalar heap'da?**
- List, Dict, Set
- Objects (class instance)
- Katta ma'lumotlar
```python
# Heap'da
numbers = [1, 2, 3, 4, 5]     # List - heap
person = {"ism": "Ali"}        # Dict - heap
data = set([1, 2, 3])          # Set - heap

class Student:
    pass

talaba = Student()             # Object - heap
```

## Vizualizatsiya
```
STACK (Tez, Kichik)          HEAP (Sekinroq, Katta)
+------------------+          +----------------------+
| x = 5            |          | numbers = [1,2,3,4,5]|
| y = 10           |    →     | person = {...}       |
| name (reference) |-------→  | "Ali" (actual string)|
+------------------+          +----------------------+
```

## Pass by Value vs Pass by Reference

### Immutable (O'zgarmas) - Pass by Value
```python
# int, float, str, tuple - immutable

def ozgartir(x):
    x = 100
    print(f"Funksiya ichida: {x}")

a = 5
ozgartir(a)
print(f"Funksiya tashqarida: {a}")  # 5 - o'zgarmadi!
```

### Mutable (O'zgaruvchan) - Pass by Reference
```python
# list, dict, set - mutable

def ozgartir_list(lst):
    lst.append(100)
    print(f"Funksiya ichida: {lst}")

numbers = [1, 2, 3]
ozgartir_list(numbers)
print(f"Funksiya tashqarida: {numbers}")  # [1,2,3,100] - o'zgardi!
```

## Xotira samaradorligi

### Yomon misol (Ko'p xotira):
```python
# Har safar yangi list yaratiladi
def yomon_usul(n):
    result = []
    for i in range(n):
        result = result + [i]  # Yangi list!
    return result
```

### Yaxshi misol (Kam xotira):
```python
# Mavjud list'ga qo'shiladi
def yaxshi_usul(n):
    result = []
    for i in range(n):
        result.append(i)  # O'sha list!
    return result
```

## Shallow Copy vs Deep Copy

### Shallow Copy (Yuzaki nusxa)
```python
import copy

original = [1, 2, [3, 4]]
shallow = copy.copy(original)

shallow[2][0] = 999
print(original)  # [1, 2, [999, 4]] - o'zgardi!
```

### Deep Copy (Chuqur nusxa)
```python
import copy

original = [1, 2, [3, 4]]
deep = copy.deepcopy(original)

deep[2][0] = 999
print(original)  # [1, 2, [3, 4]] - o'zgarmadi!
```

## Memory Leaks (Xotira oqishi)

Python'da **Garbage Collector** avtomatik tozalaydi, lekin ba'zan muammo bo'lishi mumkin:
```python
# Yomon - Circular Reference
class Node:
    def __init__(self):
        self.next = None

a = Node()
b = Node()
a.next = b
b.next = a  # Circular!

# Yaxshi - None bilan tozalash
a.next = None
b.next = None
```

## Xulosa

-  Stack - tez, kichik, avtomatik
-  Heap - katta, sekinroq, qo'lda boshqarish
-  Immutable vs Mutable
-  Shallow vs Deep Copy
-  Xotira samaradorligi muhim!

## Maslahat

1. **Immutable** ishlatish - xavfsizroq
2. **Kerakli joyda copy** qiling
3. **Unnecessary objects** yaratmang
4. **Memory profiling** - katta loyihalarda