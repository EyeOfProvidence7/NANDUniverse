import unittest
import nand_components as nc

class TestNandGate(unittest.TestCase):
    def test_nand(self):
        nand_gate = nc.NandGate()
        self.assertEqual(nand_gate.compute(0, 0), 1)
        self.assertEqual(nand_gate.compute(0, 1), 1)
        self.assertEqual(nand_gate.compute(1, 0), 1)
        self.assertEqual(nand_gate.compute(1, 1), 0)

class TestNot(unittest.TestCase):
    def test_compute(self):
        not_gate = nc.Not()
        self.assertEqual(not_gate.compute([0]), [1])
        self.assertEqual(not_gate.compute([1]), [0])

class TestAnd(unittest.TestCase):
    def test_compute(self):
        and_gate = nc.And()
        self.assertEqual(and_gate.compute([0, 0]), [0])
        self.assertEqual(and_gate.compute([0, 1]), [0])
        self.assertEqual(and_gate.compute([1, 0]), [0])
        self.assertEqual(and_gate.compute([1, 1]), [1])

class TestOr(unittest.TestCase):
    def test_compute(self):
        or_gate = nc.Or()
        self.assertEqual(or_gate.compute([0, 0]), [0])
        self.assertEqual(or_gate.compute([0, 1]), [1])
        self.assertEqual(or_gate.compute([1, 0]), [1])
        self.assertEqual(or_gate.compute([1, 1]), [1])

class TestXor(unittest.TestCase):
    def test_compute(self):
        xor_gate = nc.Xor()
        self.assertEqual(xor_gate.compute([0, 0]), [0])
        self.assertEqual(xor_gate.compute([0, 1]), [1])
        self.assertEqual(xor_gate.compute([1, 0]), [1])
        self.assertEqual(xor_gate.compute([1, 1]), [0])

class TestHalfAdder(unittest.TestCase):
    def test_compute(self):
        half_adder = nc.HalfAdder()
        self.assertEqual(half_adder.compute([0, 0]), [0, 0])
        self.assertEqual(half_adder.compute([0, 1]), [1, 0])
        self.assertEqual(half_adder.compute([1, 0]), [1, 0])
        self.assertEqual(half_adder.compute([1, 1]), [0, 1])

class TestFullAdder(unittest.TestCase):
    def test_compute(self):
        full_adder = nc.FullAdder()
        self.assertEqual(full_adder.compute([0, 0, 0]), [0, 0])
        self.assertEqual(full_adder.compute([0, 0, 1]), [1, 0])
        self.assertEqual(full_adder.compute([0, 1, 0]), [1, 0])
        self.assertEqual(full_adder.compute([0, 1, 1]), [0, 1])
        self.assertEqual(full_adder.compute([1, 0, 0]), [1, 0])
        self.assertEqual(full_adder.compute([1, 0, 1]), [0, 1])
        self.assertEqual(full_adder.compute([1, 1, 0]), [0, 1])
        self.assertEqual(full_adder.compute([1, 1, 1]), [1, 1])

class TestEightBitRippleCarryAdder(unittest.TestCase):
    def setUp(self):
        self.eight_bit_adder = nc.EightBitRippleCarryAdder()

    def test_compute_no_carry(self):
        # 00000011 (3) + 00000100 (4) = 00000111 (7)
        self.assertEqual(self.eight_bit_adder.compute([0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0]), [0, 0, 0, 0, 0, 0, 1, 1, 1])

    def test_compute_with_final_carry(self):
        # 10011001 (153) + 01111011 (123) = 100010100 (276)
        self.assertEqual(self.eight_bit_adder.compute([1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1]), [1, 0, 0, 0, 1, 0, 1, 0, 0])

    def test_compute_all_zeros(self):
        # 00000000 (0) + 00000000 (0) = 000000000 (0)
        self.assertEqual(self.eight_bit_adder.compute([0] * 16), [0] * 9)

    def test_compute_all_ones(self):
        # 11111111 (255) + 11111111 (255) = 111111110 (510)
        self.assertEqual(self.eight_bit_adder.compute([1] * 16), [1, 1, 1, 1, 1, 1, 1, 1, 0])

    def test_compute_mixed_inputs(self):
        # 01100110 (102) + 10011001 (153) = 11111111 (255)
        self.assertEqual(self.eight_bit_adder.compute([0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1]), [0, 1, 1, 1, 1, 1, 1, 1, 1])

    def test_compute_with_carry_in_between(self):
        # 01111111 (127) + 00000001 (1) = 10000000 (128)
        self.assertEqual(self.eight_bit_adder.compute([0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1]), [0, 1, 0, 0, 0, 0, 0, 0, 0])

    def test_compute_overflow(self):
        # 10000000 (128) + 10000000 (128) = 100000000 (256)
        self.assertEqual(self.eight_bit_adder.compute([1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), [1, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_compute_with_alternating_bits(self):
        # 10101010 (170) + 01010101 (85) = 11111111 (255)
        self.assertEqual(self.eight_bit_adder.compute([1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1]), [0, 1, 1, 1, 1, 1, 1, 1, 1])

    def test_compute_large_sum_with_carry(self):
        # 11001100 (204) + 00110011 (51) = 11111111 (255)
        self.assertEqual(self.eight_bit_adder.compute([1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1]), [0, 1, 1, 1, 1, 1, 1, 1, 1])

    def test_compute_max_carry(self):
        # 11111111 (255) + 00000001 (1) = 100000000 (256)
        self.assertEqual(self.eight_bit_adder.compute([1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1]), [1, 0, 0, 0, 0, 0, 0, 0, 0])


if __name__ == "__main__":
    unittest.main()
