# Algoritm va Algebra

## Algoritm ta'rifi

**Algoritm** - bu muammoni yechish uchun aniq, cheklangan ko'rsatmalar ketma-ketligi.

### Algoritm xususiyatlari

1. **Aniq (Definiteness)** - har bir qadam aniq va bir ma'noli
2. **Kiruvchi (Input)** - 0 yoki undan ko'p kiruvchi ma'lumotlar
3. **Chiquvchi (Output)** - kamida bitta natija
4. **Cheklangan (Finiteness)** - albatta tugaydi
5. **Samarali (Effectiveness)** - har bir qadamni bajarish mumkin

## Psevdokod

Psevdokod - bu algoritmni oddiy tilda yozish usuli.

### Misol: Ikkita sonni almashtirish
```
ALGORITM: SonlarniAlmashtirish
KIRUVCHI: a, b
CHIQUVCHI: almashtirilgan a va b

1. temp = a
2. a = b
3. b = temp
4. TUGADI
```

### Python'da:
```python
a = 5
b = 10

# Oddiy usul
temp = a
a = b
b = temp

# Python'dagi qisqa usul
a, b = b, a

print(a, b)  # 10, 5
```

## Algoritmni tahlil qilish

Algoritmni tahlil qilishda 2 ta asosiy savol:

1. **To'g'ri ishlayaptimi?** (Correctness)
2. **Qanchalik samarali?** (Efficiency)

### Misol: Yig'indi hisoblash
```python
# Variant 1: Loop
def yigindi_v1(n):
    jami = 0
    for i in range(1, n+1):
        jami += i
    return jami

# Variant 2: Formula (Gauss formulasi)
def yigindi_v2(n):
    return n * (n + 1) // 2

print(yigindi_v1(100))  # 5050
print(yigindi_v2(100))  # 5050
```

**Savol**: Qaysi biri samaraliroq?

## Iterativ vs Rekursiv

### Iterativ (Loop bilan):
```python
def faktorial_iterativ(n):
    natija = 1
    for i in range(1, n+1):
        natija *= i
    return natija
```

### Rekursiv (O'zini chaqirish):
```python
def faktorial_rekursiv(n):
    if n == 0 or n == 1:
        return 1
    return n * faktorial_rekursiv(n - 1)
```

## Xulosa

-  Algoritm - aniq ko'rsatmalar ketma-ketligi
-  Psevdokod - algoritmni tushunish uchun
-  Har doim to'g'rilik va samaradorlikni tekshiring
-  Iterativ va rekursiv usullar mavjud