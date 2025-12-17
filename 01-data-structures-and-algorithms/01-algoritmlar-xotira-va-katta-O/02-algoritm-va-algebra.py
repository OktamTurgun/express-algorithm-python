"""
02. Algoritm va Algebra - Amaliy misollar
"""


# 1. Sonlarni almashtirish
def sonlarni_almashtirish(a, b):
    """
    Ikki sonni almashtiradi
    
    Returns:
        tuple: (a, b) almashtirilgan holda
    """
    # Variant 1: Temp variable
    temp = a
    a = b
    b = temp
    return a, b


def sonlarni_almashtirish_v2(a, b):
    """Python'dagi qisqa usul"""
    a, b = b, a
    return a, b


# 2. Yig'indi hisoblash
def yigindi_loop(n):
    """
    1 dan n gacha sonlar yig'indisi (Loop bilan)
    
    Time: O(n)
    Space: O(1)
    """
    jami = 0
    for i in range(1, n + 1):
        jami += i
    return jami


def yigindi_formula(n):
    """
    1 dan n gacha sonlar yig'indisi (Gauss formulasi)
    
    Formula: n * (n + 1) / 2
    
    Time: O(1) - Ancha tez!
    Space: O(1)
    """
    return n * (n + 1) // 2


# 3. Faktorial - Iterativ vs Rekursiv
def faktorial_iterativ(n):
    """
    Faktorial (iterativ usul)
    
    Time: O(n)
    Space: O(1)
    """
    natija = 1
    for i in range(1, n + 1):
        natija *= i
    return natija


def faktorial_rekursiv(n):
    """
    Faktorial (rekursiv usul)
    
    Time: O(n)
    Space: O(n) - rekursiya uchun
    """
    if n == 0 or n == 1:
        return 1
    return n * faktorial_rekursiv(n - 1)


# 4. Fibonacci
def fibonacci_iterativ(n):
    """
    n-chi Fibonacci soni (iterativ)
    
    Time: O(n)
    Space: O(1)
    """
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibonacci_rekursiv(n):
    """
    n-chi Fibonacci soni (rekursiv)
    
    Time: O(2^n) - Juda sekin!
    Space: O(n)
    """
    if n <= 1:
        return n
    return fibonacci_rekursiv(n - 1) + fibonacci_rekursiv(n - 2)


# TESTLAR
if __name__ == "__main__":
    print("=" * 60)
    print("ALGORITM VA ALGEBRA - MISOLLAR")
    print("=" * 60)
    
    # Test 1: Almashtirish
    print("\n 1  Sonlarni almashtirish:")
    a, b = 5, 10
    print(f"   Avval: a={a}, b={b}")
    a, b = sonlarni_almashtirish(a, b)
    print(f"   Keyin: a={a}, b={b}")
    
    # Test 2: Yig'indi
    print("\n 2  Yig'indi hisoblash (1+2+...+100):")
    n = 100
    print(f"   Loop usuli:    {yigindi_loop(n)}")
    print(f"   Formula usuli: {yigindi_formula(n)}")
    
    # Tezlikni solishtirish
    import time
    
    start = time.time()
    for _ in range(10000):
        yigindi_loop(100)
    loop_time = time.time() - start
    
    start = time.time()
    for _ in range(10000):
        yigindi_formula(100)
    formula_time = time.time() - start
    
    print(f"\n   Tezlik solishtirish (10000 marta):")
    print(f"   Loop:    {loop_time:.4f}s")
    print(f"   Formula: {formula_time:.4f}s")
    print(f"   Formula {loop_time/formula_time:.1f}x tezroq!")
    
    # Test 3: Faktorial
    print("\n 3  Faktorial:")
    for n in [5, 10, 15]:
        iter_result = faktorial_iterativ(n)
        rek_result = faktorial_rekursiv(n)
        print(f"   {n}! = {iter_result}")
        assert iter_result == rek_result, "Xato!"
    
    # Test 4: Fibonacci
    print("\n 4  Fibonacci ketma-ketligi:")
    print("   Dastlabki 10 ta son:")
    for i in range(10):
        print(f"   F({i}) = {fibonacci_iterativ(i)}")
    
    print("\n Rekursiv Fibonacci juda sekin!")
    print("   F(30) hisoblash:")
    
    start = time.time()
    iter_fib = fibonacci_iterativ(30)
    iter_time = time.time() - start
    print(f"   Iterativ: {iter_fib} ({iter_time:.4f}s)")
    
    start = time.time()
    rek_fib = fibonacci_rekursiv(30)
    rek_time = time.time() - start
    print(f"   Rekursiv: {rek_fib} ({rek_time:.4f}s)")
    print(f"   Rekursiv {rek_time/iter_time:.0f}x sekinroq! 🐌")
    
    print("\n" + "=" * 60)
    print("Barcha testlar muvaffaqiyatli!")
    print("=" * 60)