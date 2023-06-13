def is_even(number):
    last_bit = number & 1
    return last_bit == 0


print(is_even(2494563894038**2))
print(is_even(24945638940387**3))
print(is_even(1056897**2))

