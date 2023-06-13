def prime_generator(n):
    primes = []
    num = 2
    while num <= n:
        for p in primes:
            if num % p == 0:
                break
        else:
            primes.append(num)
            yield num
        num += 1


print(list(prime_generator(10)))
