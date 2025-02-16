from itertools import product

def generate_combinations(n: int) -> list[list[int]]:
    return [list(combination) for combination in product([0, 1], repeat=n)]