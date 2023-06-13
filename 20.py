def generate_cube_numbers(n):
    num = 2
    while True:
        cube = num ** 3
        if cube >= n:
            return
        yield cube
        num += 1


print(list(generate_cube_numbers(100)))
print(list(generate_cube_numbers(10)))
