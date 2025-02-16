from itertools import product
from nand_components import *

def generate_combinations(n: int) -> list[list[int]]:
    return [list(combination) for combination in product([0, 1], repeat=n)]

n = 1
combinations = generate_combinations(n)
not_gate = Not()
for combo in combinations:
    print(f"{combo} = {not_gate.compute(combo)}")
    print(f"Call count: {not_gate.nand_gate.call_count}")
    not_gate.nand_gate.call_count = 0