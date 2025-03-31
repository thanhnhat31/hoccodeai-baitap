
def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

max_prime = 0
for i in range(1, 11):
    if is_prime(i):
        max_prime = i

print(max_prime)