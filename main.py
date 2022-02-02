inp = int(input("Zadejte číslo: "))


def left_prime_number(inp):
    prime_left = True
    while prime_left:
        if prime_function(inp):
            inp -= 1
        else:
            prime_left = False
    left = inp
    return left


def right_prime_number(inp):
    prime_right = True
    while prime_right:
        if prime_function(inp):
            inp += 1
        else:
            prime_right = False
    right = inp
    return right


def prime_function(num):
    not_prime_number = False
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                not_prime_number = True
    return not_prime_number


if prime_function(inp):
    print(f"{inp} Není prvočíslo, nejližší prvočísla jsou {left_prime_number(inp), right_prime_number(inp)}")
else:
    print(f"{inp} je prvočíslo.")
