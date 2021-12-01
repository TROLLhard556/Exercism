def convert(number):
    a = ''
    b = ''
    c = ''
    if number % 3 == 0:
        a = "Pling"
    if number % 5 == 0:
        b = "Plang"
    if number % 7 == 0:
        c = "Plong"
    else:
        return number

    str = f"{a+b+c}"
    return str
