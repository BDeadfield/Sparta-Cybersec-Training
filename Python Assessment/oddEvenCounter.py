def odd_even_counter(number):
    even = 0
    odd = 0

    for value in range(number + 1):
        if value % 2 == 0:
            even += value
        else:
            odd += value

    return [even, odd]

print(odd_even_counter(5))
