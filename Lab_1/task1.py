# Програма для виводу всіх простих чисел, які розташовані між числами a та b, які задає користувач (не обов'язково a<b) .

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(a, b):
    if a > b:
        a, b = b, a
    primes = []
    for num in range(a, b + 1):
        if is_prime(num):
            primes.append(num)
    return primes

if __name__ == "__main__":
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    primes = find_primes(a, b)
    print(f"Prime numbers between {a} and {b}: {primes}")
