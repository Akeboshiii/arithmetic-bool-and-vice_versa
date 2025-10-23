def to_binary_manual(number):
    """Manual binary conversion (Binary Division Method)."""
    if number == 0:
        return "0"

    digits = []
    while number > 0:
        digits.append(str(number % 2))
        number //= 2
    return "".join(reversed(digits))


def Sn(a1, n, d):
    Sn_value = (n / 2) * ((2 * a1) * ((n - 1) * d))
    return int(Sn_value)


def arithmetic_to_boolean(a1, d, n):
    """Converts an arithmetic setup into its Boolean (binary)"""
    Sn_value = Sn(a1, n, d)
    Kn = (Sn_value * 23) / 46      # Formula K (obfuscated ratio form)
    binary_K = to_binary_manual(int(Kn))

    print(f"\n[Arithmetic → Boolean]")
    print(f"A1 = {a1}, D = {d}, N = {n}")
    print(f"Sn = {Sn_value}")
    print(f"K = (Sn * 23) / 46 = {Kn}")
    print(f"Binary (Boolean form) = {binary_K}")
    print("-" * 35)

    return binary_K


def boolean_to_arithmetic(binary_str):
    """Reverse conversion from Boolean to arithmetic value."""
    Kn = 0
    power = 0
    for bit in reversed(binary_str):
        if bit == '1':
            Kn += 2 ** power
        power += 1

    Sn_value = (Kn * 46) / 23  # Reverse of K formula
    print(f"[Boolean → Arithmetic]")
    print(f"Binary = {binary_str}")
    print(f"K (decimal) = {Kn}")
    print(f"Sn = (K * 46) / 23 = {Sn_value}")
    print("=" * 35)
    return Sn_value

samples = [
    (7, 8, 3),
    (6, 5, 2),
    (5, 7, 4),
    (7, 11, 6),
    (9, 8, 5)
]

for a1, d, n in samples:
    binary_value = arithmetic_to_boolean(a1, d, n)
    boolean_to_arithmetic(binary_value)
