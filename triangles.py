def generate(max_num: int):
    triangles = ['triangles', 1,]
    x = 1
    while triangles[-1] < max_num:
        x += 1
        triangles.append((x*(x+1))/2)
        #    print((x*(x+1))/2)
    return triangles