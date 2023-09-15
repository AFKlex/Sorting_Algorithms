import random

def generate_random_array(size:int):
    array = []
    for _ in range(size):
        array.append(random.randint(0,2147483647))
    return array
