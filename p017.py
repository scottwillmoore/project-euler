ones = "one, two, three, four, five, six, seven, eight, nine"
ones = ones.split(", ")
ones.insert(0, None)

teens = "ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen"
teens = teens.split(", ")

tens = "ten, twenty, thirty, fourty, fifty, sixty, seventy, eighty, ninety"
tens = tens.split(", ")
tens.insert(0, None)

c = 0
for n in range(1, 1000 + 1):
    d = lambda x: n // x % 10

    d1 = d(1)
    d10 = d(10)
    d100 = d(100)
    d1000 = d(1000)

    l = []

    if d1000 > 0:
        l.append("one thousand")

    if d100 > 0:
        l.append(ones[d100])
        l.append("hundred")

        if d10 > 0 or d1 > 0:
            l.append("and")

    if d10 == 1:
        l.append(teens[d1])
    else:
        if d10 > 0:
            l.append(tens[d10])

        if d1 > 0:
            l.append(ones[d1])

    s = " ".join(l)
    c += len(s) - s.count(" ")

print(c)
