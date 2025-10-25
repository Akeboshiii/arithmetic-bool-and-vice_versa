def to_binary_manual(number):
    """
    Converts a positive integer into binary manually (Binary Division Method)
    """
    if number == 0:
        return "0"

    binary_digits = []
    while number > 0:
        remainder = number % 2      # get remainder (0 or 1)
        binary_digits.append(str(remainder))
        number //= 2                # divide by 2 (integer division)

    binary_digits.reverse()         # reverse because remainders are backwards
    return "".join(binary_digits)


def arithmetic_to_boolean(a1, n, d):
    """
    Converts an arithmetic sequence into its Boolean (binary) form
    using the formula: Kn = Sn / 2  (scaled version)
    To keep decimals accurate, we multiply both sides by 2 so we store 2*Kn as integer.
    """
    Sn = (n / 2) * (2 * a1 + (n - 1) * d)  # Sum of sequence
    Kn = Sn / 2                            # Main formula
    scaled_K = Kn * 2                      # Scale to keep .5 accuracy
    binary_K = to_binary_manual(int(round(scaled_K)))  # Convert scaled value to binary

    print(f"\n[Arithmetic → Boolean]")
    print(f"A1 = {a1}, d = {d}, n = {n}")
    print(f"Sn = {Sn}")
    print(f"K = Sn/2 = {Kn}")
    print(f"Scaled (2*Kn) = {scaled_K}")
    print(f"Binary (Boolean form) = {binary_K}\n")
    return binary_K


def boolean_to_arithmetic(binary_str):
    """
    Converts a Boolean (binary) value back into arithmetic form
    using the reverse of the scaled method: Sn = (scaled_value / 2) * 2
    """
    scaled_value = 0
    power = 0
    for bit in reversed(binary_str):
        if bit == '1':
            scaled_value += 2 ** power
        power += 1

    Kn = scaled_value / 2  # undo scaling
    Sn = Kn * 2            # reverse formula Sn = Kn * 2

    print(f"[Boolean → Arithmetic]")
    print(f"Binary = {binary_str}")
    print(f"Scaled value = {scaled_value}")
    print(f"Kn (decimal) = {Kn}")
    print(f"Sn = {Sn}\n")
    return Sn


# print(to_binary_manual(23))

# Examples
binary1 = arithmetic_to_boolean(7, 3, 8)
boolean_to_arithmetic(binary1)
print("-" * 20)

binary2 = arithmetic_to_boolean(6, 2, 5)
boolean_to_arithmetic(binary2)
print("-" * 20)

binary3 = arithmetic_to_boolean(5, 7, 4)
boolean_to_arithmetic(binary3)
print("-" * 20)

binary4 = arithmetic_to_boolean(7, 11, 6)
boolean_to_arithmetic(binary4)
print("-" * 20)

binary5 = arithmetic_to_boolean(9, 8, 5)
boolean_to_arithmetic(binary5)
print("-" * 20)
