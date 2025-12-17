#Single digit looped list + squared counterparts
single_digits = range(0, 10)
squares = []
for digit in single_digits:
  if digit > -1:
    print(digit)
    squares.append(digit ** 2)
    print(squares)
print("--------Comprehensive Cubed list--------")
cubes = [num ** 3 for num in single_digits]
print(cubes)
