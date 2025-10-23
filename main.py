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


def arithmetic_to_boolean(a1, d, n):
    """
    Converts an arithmetic sequence into its Boolean (binary) form
    using the formula: Kn = (Sn * 23) / 46
    """
    Sn = (n / 2) * (2 * a1 + (n - 1) * d)  # Sum of sequence
    Kn = (Sn * 23) / 46                    # Updated Formula
    binary_K = to_binary_manual(int(Kn))   # Convert manually to binary

    print(f"\n[Arithmetic → Boolean]")
    print(f"A1 = {a1}, d = {d}, n = {n}")
    print(f"Sn = {Sn}")
    print(f"K = Sn(23)/46 = {Kn}")
    print(f"Binary (Boolean form) = {binary_K}")
    print("\n")
    return binary_K


def boolean_to_arithmetic(binary_str):
    """
    Converts a Boolean (binary) value back into arithmetic form
    using the reverse formula: Sn = (Kn * 46) / 23
    """
    Kn = 0
    power = 0
    for bit in reversed(binary_str):
        if bit == '1':
            Kn += 2 ** power
        power += 1

    Sn = (Kn * 46) / 23  # Reverse Formula

    print(f"[Boolean → Arithmetic]")
    print(f"Binary = {binary_str}")
    print(f"K (decimal) = {Kn}")
    print(f"Sn = K(46)/23 = {Sn}")
    print("\n")
    return Sn


# Examples

binary1 = arithmetic_to_boolean(7, 3, 8)
boolean_to_arithmetic(binary1)
print("-" * 20)

binary2 = arithmetic_to_boolean(6, 5, 6)
boolean_to_arithmetic(binary2)
print("-" * 20)

binary3 = arithmetic_to_boolean(5, 7, 4)
boolean_to_arithmetic(binary3)
print("-" * 20)

binary4 = arithmetic_to_boolean(4, 11, 6)
boolean_to_arithmetic(binary4)
print("-" * 20)

binary5 = arithmetic_to_boolean(5, 15, 5)
boolean_to_arithmetic(binary5)
print("-" * 20)