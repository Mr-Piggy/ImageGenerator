
from PIL import Image

colours = {'primes': (255,0,0), 'fibonacci': (0,255,0), 'squares': (0,0,255), 'triangles': (255,255,0), 'cubes': (0,255,255), 'tables': (255,0,255)}

def colour(i: int, sequences: list, colours: dict):
    for sequence in sequences:
        if i in sequence:
            return colours[sequence[0]]
    return (0,0,0)


def image(x_size: int, y_size: int,  sequences: list, colours: dict):
    if y_size == 0:
        y_size = x_size
    image = Image.new("RGB", (x_size, y_size), "black")
    for y in range(y_size):
        for x in range(x_size):
            image.putpixel((x, y), colour(x + y * x_size + 1, sequences, colours))
    image.save("image.png")
    image.show()
