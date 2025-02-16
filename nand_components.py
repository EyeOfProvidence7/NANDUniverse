class NandGate:
    def compute(self, a: int, b: int) -> int:
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

    def countNandGates(self) -> int:
        raise ValueError("Not implemented!")


#-------------------------------------------------------------------------------------------------#
        
class Not(Component):
    def __init__(self):
        super().__init__(num_inputs=1, num_outputs=1)
        self.nand_gate = NandGate()

    def _compute(self, inputs: list[int]) -> list[int]:
        a = inputs[0]
        return [self.nand_gate.compute(a, a)]
    
    def countNandGates(self) -> int:
        return 1


class And(Component):
    def __init__(self):
        super().__init__(num_inputs=2, num_outputs=1)
        self.not_gate = Not()
        self.nand_gate = NandGate()

    def _compute(self, inputs: list[int]) -> list[int]:
        a, b = inputs
        nand_out = self.nand_gate.compute(a, b)
        return [self.not_gate.compute([nand_out])[0]]
    
    def countNandGates(self):
        return self.not_gate.countNandGates() + 1


class Or(Component):
    def __init__(self):
        super().__init__(num_inputs=2, num_outputs=1)
        self.not_gate = Not()
        self.nand_gate = NandGate()

    def _compute(self, inputs: list[int]) -> list[int]:
        a, b = inputs
        not_a = self.not_gate.compute([a])[0]
        not_b = self.not_gate.compute([b])[0]
        return [self.nand_gate.compute(not_a, not_b)]
    
    def countNandGates(self):
        return self.not_gate.countNandGates() + 1
    

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
    
    def countNandGates(self):
        return self.and_gate.countNandGates() + self.or_gate.countNandGates() + self.not_gate.countNandGates()
    

class HalfAdder(Component):
    def __init__(self):
        super().__init__(num_inputs=2, num_outputs=2)  
        self.xor_gate = Xor()
        self.and_gate = And()

    def _compute(self, inputs: list[int]) -> list[int]:
        a, b = inputs
        sum_out = self.xor_gate.compute([a, b])[0]
        carry_out = self.and_gate.compute([a, b])[0] 
        return [sum_out, carry_out] 
    
    def countNandGates(self):
        return self.xor_gate.countNandGates() + self.and_gate.countNandGates()
    

class FullAdder(Component):
    def __init__(self):
        super().__init__(num_inputs=3, num_outputs=2)
        self.half_adder1 = HalfAdder()
        self.half_adder2 = HalfAdder()
        self.or_gate = Or()

    def _compute(self, inputs: list[int]) -> list[int]:
        a, b, carry_in = inputs
        half1_sum, half1_carry = self.half_adder1.compute([a, b])
        half2_sum, half2_carry = self.half_adder2.compute([half1_sum, carry_in])
        carry_out = self.or_gate.compute([half1_carry, half2_carry])[0]

        return [half2_sum, carry_out]
    
    def countNandGates(self):
        return self.half_adder1.countNandGates() * 2 + self.or_gate.countNandGates()
    

class EightBitRippleCarryAdder(Component):
    def __init__(self):
        # 8 bits of A + 8 bits of B = 16 inputs; 8-bit sum + carry out = 9 outputs
        super().__init__(num_inputs=16, num_outputs=9)
        self.full_adder = FullAdder()

    def _compute(self, inputs: list[int]) -> list[int]:
        a = list(reversed(inputs[:8]))
        b = list(reversed(inputs[8:]))

        carry_in = 0
        sum_bits = []

        for i in range(8):
            sum_i, carry_out_i = self.full_adder.compute([a[i], b[i], carry_in])
            sum_bits.append(sum_i)
            carry_in = carry_out_i

        return list(reversed(sum_bits + [carry_in]))
    
    def countNandGates(self):
        return self.full_adder.countNandGates()


class DLatch(Component):
    # A simple 1-bit storage made up of 4 NAND gates and a NOT gate.
    # Takes a "data" bit, followed by an "enable" bit. When "enable" is set to
    # 1, then the "data" bit is saved as the current state.
    # Output for this component is [state, NOT state].
    # https://www.build-electronic-circuits.com/d-latch/
    def __init__(self, initial_state: int = 0):
        super().__init__(num_inputs=2, num_outputs=2)
        self.state = initial_state
        self.nand_gates = [NandGate() for _ in range(4)]
        self.not_gate = Not()
    
    def _compute(self, inputs: list[int]) -> list[int]:
        # First input is data, second is "enable", or clock switch.
        d = inputs[0]
        e = inputs[1]
        g1 = self.nand_gates[0].compute(d, e)
        n = self.not_gate.compute([d])[0]
        g2 = self.nand_gates[1].compute(e, n)

        g3 = self.nand_gates[2].compute(g1, 0 if self.state else 1)
        g4 = self.nand_gates[3].compute(g3, g2)
        g3 = self.nand_gates[2].compute(g1, g4) # Compute 3rd NAND gate again after signal propagation.
        self.state = g3

        return [self.state, g4]
    
    def countNandGates(self):
        return len(self.nand_gates) + self.not_gate.countNandGates()


#-------------------------------------------------------------------------------------------------#