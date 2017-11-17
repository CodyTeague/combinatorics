primes = [2]

def is_prime(n):
    global primes
    for i in range(primes[-1]+1,n+1):
        factor = False
        for prime in primes:
            if i % prime == 0:
                factor = True
        if not factor:
            primes.append(i)

    return (n in primes)

def prime_factorization(n):
    prime_factors = []
    if is_prime(n):
        return [1,n]
    for prime in primes:
        if n % prime == 0:
            n = n / prime
            if prime not in prime_factors:
                prime_factors.append(prime)
    return prime_factors

def count_prime_factorization(n,arr):
    prime_factors = prime_factorization(n)
    count = 0
    for i in arr:
        common = False
        for prime in prime_factors:
            if i % prime == 0:
                common = True
        if not common:
            count += 1
    return count

print(count_prime_factorization(210,range(1,1001)))
