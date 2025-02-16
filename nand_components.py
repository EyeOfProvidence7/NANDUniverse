class NandGate:
    @staticmethod
    def nand(a: int, b: int) -> int:
        return 1 - (a & b)


class Component:
    def __init__(self, num_inputs: int, num_outputs: int):
        self.num_inputs = num_inputs
        self.num_outputs = num_outputs

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
        return [NandGate.nand(inputs[0], inputs[0])]


class And(Component):
    def __init__(self):
        super().__init__(num_inputs=2, num_outputs=1)
        self.not_gate = Not()

    def _compute(self, inputs: list[int]) -> list[int]:
        nand_out = NandGate.nand(inputs[0], inputs[1])
        return [self.not_gate.compute([nand_out])[0]]


class Or(Component):
    def __init__(self):
        super().__init__(num_inputs=2, num_outputs=1)

    def _compute(self, inputs: list[int]) -> list[int]:
        a, b = inputs
        not_a = NandGate.nand(a, a)
        not_b = NandGate.nand(b, b)
        return [NandGate.nand(not_a, not_b)]
    

#-------------------------------------------------------------------------------------------------#