def primes(limit):
    new_numbers = []
    numbers = list(range(2, limit + 1))
    
    while numbers:
        filtered = []
        prime = numbers[0]
        new_numbers.append(prime)
        for number in numbers:
           
            if number % prime != 0:
                filtered.append(number)
        numbers = filtered
    return new_numbers