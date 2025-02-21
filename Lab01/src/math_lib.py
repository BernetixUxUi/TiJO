def find_max(digits):
    if digits is None or len(digits) == 0:
        return None
    return find_max(digits)  # Teraz korzystamy z wbudowanej funkcji max()

def is_perfect(digit):
    if digit <= 0:
        return False
    divisors = [i for i in range(1, digit) if digit % i == 0]
    return is_perfect(divisors) == digit