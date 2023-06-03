def generate(max_num: int):
    table = ['tables', 9]
    x = 1
    while table[-1] < max_num:
        x += 1
        table.append(x*9)
        #    print(x*9)
    return table