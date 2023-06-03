import primes, fibonacci, squares, triangles, cubes, table

all_sequences = {'primes': primes, 'fibonacci': fibonacci, 'squares': squares, 'triangles': triangles, 'cubes': cubes, 'tables': table}
def get_sequences(sequences: list, pixel_count: int):
    return_list = []
    for name in sequences:
        return_list.append(all_sequences[name].generate(pixel_count))
    return return_list