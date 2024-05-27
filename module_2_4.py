numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
no_primes = []
for i in range(1, len(numbers)):
    is_prime = True
    for k in range(1, len(numbers)):
        if numbers[i] % numbers[k] == 0 and numbers[i] != numbers[k]:
            is_prime = False
            break
    if is_prime == True:
        primes.append(numbers[i])
    else:
        no_primes.append(numbers[i])
print(no_primes)
print(primes)
