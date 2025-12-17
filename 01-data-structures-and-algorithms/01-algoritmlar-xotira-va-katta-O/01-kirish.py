"""
01. Kirish - Amaliy misollar
"""

def eng_katta_topish(sonlar):
    """Eng katta sonni topadi"""
    if not sonlar:
        return None
    
    maksimum = sonlar[0]
    for son in sonlar:
        if son > maksimum:
            maksimum = son
    return maksimum


def faktorial(n):
    """Faktorial hisoblash"""
    if n == 0 or n == 1:
        return 1
    return n * faktorial(n - 1)


if __name__ == "__main__":
    print("=" * 50)
    print("KIRISH - MISOLLAR")
    print("=" * 50)
    
    # Test 1
    sonlar = [5, 2, 9, 1, 7]
    print(f"\n1. Eng katta: {eng_katta_topish(sonlar)}")
    
    # Test 2
    print(f"\n2. Faktorial:")
    for n in [0, 1, 5]:
        print(f"   {n}! = {faktorial(n)}")
    
    print("\n" + "=" * 50)