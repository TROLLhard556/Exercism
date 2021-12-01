# 1. split number into digits 
# 2. count how many digits
# 3. num of digits = raised value
# 4. each digit gets raised to the power
# 5. results are added
# ex. 9 is True because 9^1 = 9, 10 is False because 1^2 + 0^2 = 1 =! 10


def is_armstrong_number(number):
    digits = [int(digit) for digit in str(number)]
    power = len(digits)
    equation = [digit**power for digit in digits]
    if sum(equation) == number:
         return True
    else:
        return False

