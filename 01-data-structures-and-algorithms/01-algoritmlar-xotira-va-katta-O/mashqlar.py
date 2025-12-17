"""
Mashqlar - Algoritmlar, Xotira va Big O
"""


# ==================== MASHQ 1 ====================
def mashq_1():
    """
    Mashq 1: Ikkinchi eng katta elementni toping
    
    Input: [5, 2, 9, 1, 7, 3]
    Output: 7
    
    Big O: ?
    """
    def ikkinchi_eng_katta(arr):
        # TODO: Yechimingizni yozing
        pass
    
    # Test
    test_cases = [
        ([5, 2, 9, 1, 7, 3], 7),
        ([10, 20, 4, 45, 99], 45),
        ([1, 2], 1),
    ]
    
    for arr, expected in test_cases:
        result = ikkinchi_eng_katta(arr)
        status = "✅" if result == expected else "❌"
        print(f"{status} {arr} → {result} (kutilgan: {expected})")


# ==================== MASHQ 2 ====================
def mashq_2():
    """
    Mashq 2: Palindrom tekshirish
    
    Input: "racecar"
    Output: True
    
    Big O: ?
    """
    def palindrom_mi(s):
        # TODO: Yechimingizni yozing
        pass
    
    # Test
    test_cases = [
        ("racecar", True),
        ("hello", False),
        ("madam", True),
        ("python", False),
    ]
    
    for s, expected in test_cases:
        result = palindrom_mi(s)
        status = "✅" if result == expected else "❌"
        print(f"{status} '{s}' → {result} (kutilgan: {expected})")


# ==================== MASHQ 3 ====================
def mashq_3():
    """
    Mashq 3: Dublikatlar bormi?
    
    Input: [1, 2, 3, 4, 5]
    Output: False
    
    Input: [1, 2, 3, 1]
    Output: True
    
    Big O: ?
    """
    def dublikat_bormi(arr):
        # TODO: Yechimingizni yozing
        pass
    
    # Test
    test_cases = [
        ([1, 2, 3, 4, 5], False),
        ([1, 2, 3, 1], True),
        ([1, 1, 1], True),
        ([], False),
    ]
    
    for arr, expected in test_cases:
        result = dublikat_bormi(arr)
        status = "✅" if result == expected else "❌"
        print(f"{status} {arr} → {result} (kutilgan: {expected})")


# ==================== MASHQ 4 ====================
def mashq_4():
    """
    Mashq 4: Big O ni aniqlang
    
    Quyidagi funksiyalarning Big O ni yozing
    """
    
    # 4a
    def funksiya_a(arr):
        for x in arr:
            print(x)
    # Big O: ?
    
    # 4b
    def funksiya_b(arr):
        for i in range(len(arr)):
            for j in range(len(arr)):
                print(arr[i], arr[j])
    # Big O: ?
    
    # 4c
    def funksiya_c(arr):
        for x in arr:
            print(x)
        for x in arr:
            print(x)
    # Big O: ?
    
    # 4d
    def funksiya_d(n):
        i = 1
        while i < n:
            print(i)
            i *= 2
    # Big O: ?
    
    print("4a: O(?)  ← Javobingizni yozing")
    print("4b: O(?)  ← Javobingizni yozing")
    print("4c: O(?)  ← Javobingizni yozing")
    print("4d: O(?)  ← Javobingizni yozing")


# ==================== MASHQ 5 ====================
def mashq_5():
    """
    Mashq 5: Anagramma tekshirish
    
    Ikki string anagramma mi?
    
    Input: "listen", "silent"
    Output: True
    
    Big O: ?
    """
    def anagramma_mi(s1, s2):
        # TODO: Yechimingizni yozing
        pass
    
    # Test
    test_cases = [
        ("listen", "silent", True),
        ("hello", "world", False),
        ("evil", "vile", True),
    ]
    
    for s1, s2, expected in test_cases:
        result = anagramma_mi(s1, s2)
        status = "✅" if result == expected else "❌"
        print(f"{status} '{s1}' va '{s2}' → {result} (kutilgan: {expected})")


# ==================== ASOSIY DASTUR ====================
if __name__ == "__main__":
    print("=" * 70)
    print("MASHQLAR - Algoritmlar, Xotira va Big O")
    print("=" * 70)
    
    print("\n Mashq 1: Ikkinchi eng katta")
    print("-" * 70)
    mashq_1()
    
    print("\n Mashq 2: Palindrom")
    print("-" * 70)
    mashq_2()
    
    print("\n Mashq 3: Dublikatlar")
    print("-" * 70)
    mashq_3()
    
    print("\n Mashq 4: Big O ni aniqlash")
    print("-" * 70)
    mashq_4()
    
    print("\n Mashq 5: Anagramma")
    print("-" * 70)
    mashq_5()
    
    print("\n" + "=" * 70)
    print(" Yechimlarni o'zingiz yozib ko'ring!")
    print("=" * 70)