def numbers_to_cubes(numbers):
    return [(number, number**3) for number in numbers]
numbers = [1, 2, 3, 4]
number_cubes = numbers_to_cubes(numbers)
print(number_cubes)
