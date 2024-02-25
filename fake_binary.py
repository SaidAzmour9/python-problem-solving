def fake_bin(x):
    y = ''
    if x != '':
        for i in x:
            i = int(i)
            if i < 5:
                y += '0'
            else:
                y += '1'
    return y