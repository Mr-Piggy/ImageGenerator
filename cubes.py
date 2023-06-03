def generate(max_num: int):
    cubes = ['cubes', 1]
    x = 1
    while cubes[-1] < max_num:
        x += 1
        cubes.append(x*x*x)
        #    print(x*x*x)
    return cubes