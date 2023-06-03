
def generate(max_num: int):
    fibonacci = ['fibonacci', 1,1]
    while fibonacci[-1] < max_num:
        index = len(fibonacci)
        previous = index-2
        now = index-1
        nextnumber = fibonacci[previous] + fibonacci[now]
        fibonacci.append(nextnumber)
        #    print(nextnumber)
    return fibonacci
