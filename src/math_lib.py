def find_max(digits):
    if digits is None or len(digits) == 0:
        return None
    return max(digits)  # tutaj wywołujemy wbudowaną funkcję max()

def is_perfect(digit):
    if digit <= 0:
        return False
    divisors = [i for i in range(1, digit) if digit % i == 0]
    return sum(divisors) == digit