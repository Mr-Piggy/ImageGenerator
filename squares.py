def generate(max_num: int):
    squares = ['squares',1]
    x = 1
    while squares[-1] < max_num:
        x += 1
        squares.append(x*x)
        #    print(x*x)
    return squares