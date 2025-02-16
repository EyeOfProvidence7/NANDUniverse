import unittest
from nand_components import NandGate, Not, And, Or

class TestNandGate(unittest.TestCase):
    def test_nand(self):
        nand_gate = NandGate()
        self.assertEqual(nand_gate.compute(0, 0), 1)
        self.assertEqual(nand_gate.compute(0, 1), 1)
        self.assertEqual(nand_gate.compute(1, 0), 1)
        self.assertEqual(nand_gate.compute(1, 1), 0)

class TestNot(unittest.TestCase):
    def test_compute(self):
        nand_gate = NandGate()
        not_gate = Not(nand_gate)
        self.assertEqual(not_gate.compute([0]), [1])
        self.assertEqual(not_gate.compute([1]), [0])

class TestAnd(unittest.TestCase):
    def test_compute(self):
        nand_gate = NandGate()
        not_gate = Not(nand_gate)
        and_gate = And(nand_gate, not_gate)
        self.assertEqual(and_gate.compute([0, 0]), [0])
        self.assertEqual(and_gate.compute([0, 1]), [0])
        self.assertEqual(and_gate.compute([1, 0]), [0])
        self.assertEqual(and_gate.compute([1, 1]), [1])

class TestOr(unittest.TestCase):
    def test_compute(self):
        nand_gate = NandGate()
        not_gate = Not(nand_gate)
        or_gate = Or(nand_gate, not_gate)
        self.assertEqual(or_gate.compute([0, 0]), [0])
        self.assertEqual(or_gate.compute([0, 1]), [1])
        self.assertEqual(or_gate.compute([1, 0]), [1])
        self.assertEqual(or_gate.compute([1, 1]), [1])

if __name__ == "__main__":
    unittest.main()
