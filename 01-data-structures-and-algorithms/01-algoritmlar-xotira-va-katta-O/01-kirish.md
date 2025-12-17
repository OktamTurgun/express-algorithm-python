# Kirish

## Algoritm nima?

Algoritm - bu muammoni yechish uchun aniq ko'rsatmalar ketma-ketligi.
Bir necha misol:
- Ovqat tayyorlash retsepti
- Navigatsiya yo'riqnomalari
- Kompyuter dasturlari

Algoritm samarali bo'lishi uchun:
1. Aniq bo'lishi kerak
2. Chekli qadamlar bo'lishi kerak
3. Natijaviy bo'lishi kerak

## Misol: Eng katta sonni topish
```python
def eng_katta(sonlar):
    maksimum = sonlar[0]
    for son in sonlar:
        if son > maksimum:
            maksimum = son
    return maksimum

print(eng_katta([5, 2, 9, 1]))  # 9
```

## Nega o'rganish kerak?

-  Mantiqiy fikrlash
-  Tez kod yozish
-  Interview uchun
-  Katta loyihalar