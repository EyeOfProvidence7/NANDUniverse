nand_count = 0

class NandGate:
    def compute(self, a: int, b: int) -> int:
        global nand_count
        nand_count += 1
        return 1 - (a & b)


class Component:
    def __init__(self, num_inputs: int, num_outputs: int):
        self.num_inputs = num_inputs
        self.num_outputs = num_outputs
        self.nand_gate = NandGate()

    def compute(self, inputs: list[int]) -> list[int]:
        if len(inputs) != self.num_inputs:
            raise ValueError(f"{self.__class__.__name__} expects {self.num_inputs} inputs, got {len(inputs)}")

        outputs = self._compute(inputs)

        if len(outputs) != self.num_outputs:
            raise ValueError(f"{self.__class__.__name__} must return {self.num_outputs} outputs, got {len(outputs)}")
        
        return outputs

#-------------------------------------------------------------------------------------------------#
        
class Not(Component):
    def __init__(self):
        super().__init__(num_inputs=1, num_outputs=1)

    def _compute(self, inputs: list[int]) -> list[int]:
        a = inputs[0]
        return [self.nand_gate.compute(a, a)]


class And(Component):
    def __init__(self):
        super().__init__(num_inputs=2, num_outputs=1)
        self.not_gate = Not()

    def _compute(self, inputs: list[int]) -> list[int]:
        a, b = inputs
        nand_out = self.nand_gate.compute(a, b)
        return [self.not_gate.compute([nand_out])[0]]


class Or(Component):
    def __init__(self):
        super().__init__(num_inputs=2, num_outputs=1)
        self.not_gate = Not()

    def _compute(self, inputs: list[int]) -> list[int]:
        a, b = inputs
        not_a = self.not_gate.compute([a])[0]
        not_b = self.not_gate.compute([b])[0]
        return [self.nand_gate.compute(not_a, not_b)]
    

class Xor(Component):
    def __init__(self):
        super().__init__(num_inputs=2, num_outputs=1)
        self.and_gate = And()
        self.or_gate = Or()
        self.not_gate = Not()

    def _compute(self, inputs: list[int]) -> list[int]:
        a, b = inputs
        or_out = self.or_gate.compute([a, b])[0]
        and_out = self.and_gate.compute([a, b])[0]
        not_and_out = self.not_gate.compute([and_out])[0]
        return [self.and_gate.compute([or_out, not_and_out])[0]]
    

#-------------------------------------------------------------------------------------------------#