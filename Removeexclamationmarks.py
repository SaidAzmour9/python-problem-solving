def remove_exclamation_marks(s):
    lis = list(s)
    li = []
    for i in lis:
        if i != "!":
            li.append(i)
        s = "".join(li)
    return s