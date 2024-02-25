def multiply(n):
    t = 0
    n = str(n)
    for i in n:
        if i == '-':
            continue
        t+= 1
    n = int(n)
    s = n * 5**t
    return s