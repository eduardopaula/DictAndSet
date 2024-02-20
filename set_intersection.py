from primes_and_squares import squares_generator, primes_generator
evens = set(range(0, 51, 2))
odds = set(range(1, 51, 2))

# print(evens)
# print(odds)

primes = set(primes_generator(100))
print(primes)
squares = set(squares_generator(100))
print(squares)

print(odds.intersection(squares))
print(evens & squares)

# pass an iterable to the method
even_squares = evens.intersection(squares_generator(100))
print(even_squares)

even_squares = (evens & (squares_generator(100)))
print(even_squares)
