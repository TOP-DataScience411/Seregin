def numbers_strip(numbers: list[float], n: int = 1, return_copy: bool = False) -> list[float]:

    if return_copy:
        numbers = numbers.copy()

    if n > len(numbers):
        return []
        
    for _ in range(n):
        numbers.remove(min(numbers))
        numbers.remove(max(numbers))
    
    return numbers
    
    
      # 8:42:26 > python -i 3.py
# >>> sample = [1, 2, 3, 4]
# >>> sample_stripped = numbers_strip(sample)
# >>> sample_stripped
# [2, 3]
# >>> sample is sample_stripped
# True
# >>>
