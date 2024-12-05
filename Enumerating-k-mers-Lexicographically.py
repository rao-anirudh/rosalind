bases = {"0": "A", "1": "C", "2": "G", "3": "T"}


def quart_to_dec(num):
    digits = [int(digit) for digit in str(num)]
    n = len(digits)
    dec = 0
    for i in range(0, n):
        dec += digits[i]*pow(4, n-i-1)
    return dec


def dec_to_quart(num):
    quart = []
    while num != 0:
        quart.append(str(num % 4))
        num = int(num / 4)
    return "".join(quart[::-1])


def start(n):
    return "".join(["0" for i in range(0, n)])


def sequence(num):
    return "".join(bases[digit] for digit in num)


def add(num):
    return dec_to_quart(quart_to_dec(num) + 1)

