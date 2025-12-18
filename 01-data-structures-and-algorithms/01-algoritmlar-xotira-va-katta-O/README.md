# 01. Algoritmlar, Xotira va Katta O

Bu darsda algoritm asoslari, xotira bilan ishlash va Big O notation haqida o'rganamiz.

## Mavzular

### 1. Kirish
- Algoritm nima?
- Nega algoritm o'rganish kerak?
- Algoritmning xususiyatlari
- Oddiy misollar

**Fayllar**: `01-kirish.md`, `01-kirish.py`

---

### 2. Algoritm va Algebra
- Algoritm ta'rifi
- Psevdokod
- Algoritmni tahlil qilish
- Iterativ vs Rekursiv
- Performance comparison

**Fayllar**: `02-algoritm-va-algebra.md`, `02-algoritm-va-algebra.py`

---

### 3. Xotira
- RAM vs Disk
- Stack vs Heap
- Pass by Value vs Pass by Reference
- Shallow Copy vs Deep Copy
- Xotira samaradorligi
- Memory Leaks

**Fayllar**: `03-xotira.md`, `03-xotira.py`

---

### 4. Big O (Katta O)
- Big O notation nima?
- Time Complexity
- Space Complexity
- O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ), O(n!)
- Performance comparison
- Common operations Big O

**Fayllar**: `04-big-O-katta-O.md`, `04-big-O-katta-O.py`

---

## O'rganish natijalari

Ushbu darsni tugallagandan so'ng siz:

-  Algoritm nima ekanligini tushunarli tushuntirishingiz mumkin
-  Xotira qanday ishlashini va Stack/Heap farqini bilasiz
-  Pass by Value va Pass by Reference farqini bilasiz
-  Big O notation bilan algoritmlarni tahlil qila olasiz
-  Algoritmlarning vaqt va xotira kompleksligini hisoblay olasiz
-  Iterativ va rekursiv yondashuvlarni solishtirasiz
-  Python'dagi asosiy operatsiyalarning Big O'sini bilasiz

---

## Darslar tartabi

1. **01-kirish** - Algoritmga kirish (1 soat)
2. **02-algoritm-va-algebra** - Algoritm asoslari (1.5 soat)
3. **03-xotira** - Xotira bilan ishlash (1.5 soat)
4. **04-big-O-katta-O** - Big O notation (2 soat)
5. **mashqlar** - Amaliy mashqlar (1 soat)

**Jami**: ~7 soat

---

## Qanday boshlash?

### 1. Ketma-ket o'qing
```bash
# Birinchi mavzu
python 01-kirish.py

# Ikkinchi mavzu
python 02-algoritm-va-algebra.py

# Uchinchi mavzu
python 03-xotira.py

# To'rtinchi mavzu
python 04-big-O-katta-O.py
```

### 2. Mashqlarni bajaring
```bash
python mashqlar.py
```

---

## Big O Cheat Sheet

### Time Complexity
```
Tez ←                                                    → Sekin
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)
```

### Misollar
| Big O      | Misol                          |
|------------|--------------------------------|
| O(1)       | Array index, dict lookup       |
| O(log n)   | Binary search                  |
| O(n)       | Linear search, simple loop     |
| O(n log n) | Merge sort, Quick sort         |
| O(n²)      | Bubble sort, nested loops      |
| O(2ⁿ)      | Recursive Fibonacci            |
| O(n!)      | Permutations                   |

---

## Muhim Tushunchalar

### Algoritm xususiyatlari
1. **Aniq** - har bir qadam tushunarli
2. **Cheklangan** - albatta tugaydi
3. **Kiruvchi** - 0 yoki undan ko'p input
4. **Chiquvchi** - kamida 1 ta output
5. **Samarali** - amalga oshirish mumkin

### Stack vs Heap
| Stack | Heap |
|-------|------|
| Tez | Sekinroq |
| Kichik | Katta |
| Avtomatik | Qo'lda |
| LIFO | Random |
| int, float, bool | list, dict, object |

### Big O Qoidalar
1. **Konstantalarni e'tiborsiz qoldiring**: O(2n) = O(n)
2. **Eng katta hadni oling**: O(n² + n) = O(n²)
3. **Turli o'zgaruvchilar**: O(n × m) ≠ O(n²)

---

## Mashqlar

`mashqlar.py` faylida 5 ta mashq bor:

1. **Ikkinchi eng katta** - Array manipulation
2. **Palindrom** - String manipulation
3. **Dublikatlar** - Set usage
4. **Big O aniqlash** - Time complexity
5. **Anagramma** - String comparison

Har bir mashqni mustaqil yechib ko'ring!

---

## Eslatmalar

### Performance
```python
# Yomon ❌
result = []
for i in range(n):
    result = result + [i]  # O(n²)

# Yaxshi ✅
result = []
for i in range(n):
    result.append(i)  # O(n)
```

### Mutable vs Immutable
```python
# Immutable (o'zgarmaydi)
x = 5
def change(x):
    x = 10
change(x)
print(x)  # 5

# Mutable (o'zgaradi)
lst = [1, 2, 3]
def change(lst):
    lst.append(4)
change(lst)
print(lst)  # [1, 2, 3, 4]
```

---

## Keyingi dars

Ushbu darsni tugallagandan so'ng:
- **02-array-va-string** - Array va String bilan ishlash

---

## Qo'shimcha Resurslar

### Kitoblar
- "Introduction to Algorithms" - CLRS
- "Grokking Algorithms" - Aditya Bhargava

### Online
- LeetCode - amaliy mashqlar
- HackerRank - interview preparation
- Big O Cheat Sheet - bigocheatsheet.com

### Video
- CS50 - Harvard
- freeCodeCamp - Algorithms course

---

## Checklist

Darsni tugallagandan so'ng o'zingizni tekshiring:

- [ ] Algoritm ta'rifini tushuntira olaman
- [ ] Stack va Heap farqini bilaman
- [ ] Big O notation bilan ishlashni bilaman
- [ ] O(1), O(n), O(n²) ni farqlashim mumkin
- [ ] Pass by Value va Reference farqini bilaman
- [ ] Shallow va Deep Copy ni tushunaman
- [ ] Python operatsiyalarning Big O'sini bilaman
- [ ] Barcha mashqlarni yechdim

---

## Interview Savollari

Ushbu darsdan keyin siz quyidagi savollarga javob bera olasiz:

1. **Algoritm nima?**
2. **Stack va Heap farqi nima?**
3. **Big O notation nima va nega kerak?**
4. **O(n) va O(n²) farqi nima?**
5. **List.append() qanday Big O?** (Javob: O(1))
6. **Pass by value va reference farqi?**
7. **Shallow va Deep copy farqi?**
8. **Recursive Fibonacci nega sekin?** (Javob: O(2ⁿ))

---

## Savollar?

Agar savollaringiz bo'lsa:
- Issues ochish: [GitHub Issues](https://github.com/YOUR_USERNAME/express-algorithm-python/issues)
- Muhokama: [Discussions](https://github.com/YOUR_USERNAME/express-algorithm-python/discussions)

---

## Maslahatlar

1. **Har kuni qayta ko'rib chiqing** - takrorlash muhim
2. **Misollarni o'zingiz yozing** - amaliyot qiling
3. **Mashqlarni yechishga harakat qiling** - googlemang!
4. **Vaqt oling** - shoshilmang
5. **Savollar bering** - bilmasangiz so'rang

---

**⏱ Taxminiy vaqt**: 7-8 soat  
** Qiyinlik**: Oson → O'rta  
** Progress**: 1/9 (Ma'lumot Tuzilmalari)

---

**Omad!** Keyingi darsda ko'rishguncha!