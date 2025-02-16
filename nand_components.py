class NandGate:
    def __init__(self):
        self.call_count = 0

    def compute(self, a: int, b: int) -> int:
        self.call_count += 1
        return 1 - (a & b)


class Component:
    def __init__(self, num_inputs: int, num_outputs: int, nand_gate: NandGate):
        self.num_inputs = num_inputs
        self.num_outputs = num_outputs
        self.nand_gate = nand_gate

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
        super().__init__(num_inputs=1, num_outputs=1, nand_gate=NandGate())

    def _compute(self, inputs: list[int]) -> list[int]:
        return [self.nand_gate.compute(inputs[0], inputs[0])]


class And(Component):
    def __init__(self):
        super().__init__(num_inputs=2, num_outputs=1, nand_gate=NandGate())
        self.not_gate = Not()

    def _compute(self, inputs: list[int]) -> list[int]:
        a, b = inputs
        nand_out = self.nand_gate.compute(a, b)
        return [self.not_gate.compute([nand_out])[0]]


class Or(Component):
    def __init__(self):
        super().__init__(num_inputs=2, num_outputs=1, nand_gate=NandGate())
        self.not_gate = Not()

    def _compute(self, inputs: list[int]) -> list[int]:
        a, b = inputs
        not_a = self.not_gate.compute([a])[0]
        not_b = self.not_gate.compute([b])[0]
        return [self.nand_gate.compute(not_a, not_b)]
    

#-------------------------------------------------------------------------------------------------#