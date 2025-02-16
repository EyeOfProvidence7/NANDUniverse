from itertools import product
from nand_components import *
import nand_components

def generate_combinations(n: int) -> list[list[int]]:
    return [list(combination) for combination in product([0, 1], repeat=n)]

n = 2
combinations = generate_combinations(n)
component = And()
for combo in combinations:
    print(f"{combo} = {component.compute(combo)} {nand_components.nand_count}")
    nand_components.nand_count = 0