def find_average(numbers):
    s = 0
    Le = len(numbers)
    if Le > 1:
        for i in numbers:
            s += i
            av = s / Le
        return av
    elif len(numbers) == 0:
        return 0
    else:
        return numbers[0]