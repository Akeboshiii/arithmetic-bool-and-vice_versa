def to_binary_manual(number):
    """
    Converts a positive integer or float into binary manually.
    Supports fractional (decimal) parts.
    """
    # Separate integer and fractional parts
    integer_part = int(number)
    fraction_part = number - integer_part

    # Convert integer part
    if integer_part == 0:
        integer_binary = "0"
    else:
        binary_digits = []
        while integer_part > 0:
            remainder = integer_part % 2
            binary_digits.append(str(remainder))
            integer_part //= 2
        binary_digits.reverse()
        integer_binary = "".join(binary_digits)

    # Convert fractional part (up to 8 bits for precision)
    fraction_binary = ""
    count = 0
    while fraction_part > 0 and count < 8:
        fraction_part *= 2
        bit = int(fraction_part)
        if bit == 1:
            fraction_part -= bit
            fraction_binary += "1"
        else:
            fraction_binary += "0"
        count += 1

    # Combine both parts
    if fraction_binary:
        return f"{integer_binary}.{fraction_binary}"
    else:
        return integer_binary


def arithmetic_to_boolean(a1, n, d):
    """
    Converts an arithmetic sequence into binary (Boolean form)
    using the formula: Kn = Sn / 2
    """
    Sn = (n / 2) * (2 * a1 + (n - 1) * d)
    Kn = Sn / 2
    binary_K = to_binary_manual(Kn)

    print(f"\n[Arithmetic → Boolean]")
    print(f"A1 = {a1}, d = {d}, n = {n}")
    print(f"Sn = {Sn}")
    print(f"Kn = {Kn}")
    print(f"Binary (Boolean form) = {binary_K}\n")
    return binary_K


def boolean_to_arithmetic(binary_str):
    """
    Converts a binary (Boolean) value back into arithmetic form.
    Handles fractional binary inputs.
    """
    if "." in binary_str:
        integer_str, fraction_str = binary_str.split(".")
    else:
        integer_str, fraction_str = binary_str, ""

    # Convert integer part
    integer_value = 0
    for i, bit in enumerate(reversed(integer_str)):
        if bit == '1':
            integer_value += 2 ** i

    # Convert fractional part
    fraction_value = 0
    for i, bit in enumerate(fraction_str, start=1):
        if bit == '1':
            fraction_value += 2 ** (-i)

    Kn = integer_value + fraction_value
    Sn = Kn * 2

    print(f"[Boolean → Arithmetic]")
    print(f"Binary = {binary_str}")
    print(f"Kn (decimal) = {Kn}")
    print(f"Sn = {Sn}\n")
    return Sn


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
