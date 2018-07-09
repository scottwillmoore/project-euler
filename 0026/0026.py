def recurrance(numerator, denominator):
    result = ""
    history = {}

    remainder = numerator % denominator

    while remainder != 0 and remainder not in history:
        remainder *= 10

        history[remainder] = len(result)

        quotient = remainder // denominator
        result += str(quotient)

        remainder = remainder % denominator
        print(remainder)

    return result


print(recurrance(1, 9))
