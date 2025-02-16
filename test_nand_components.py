import unittest
from nand_components import NandGate, Not, And, Or

class TestNandGate(unittest.TestCase):
    def test_nand(self):
        self.assertEqual(NandGate.nand(0, 0), 1)
        self.assertEqual(NandGate.nand(0, 1), 1)
        self.assertEqual(NandGate.nand(1, 0), 1)
        self.assertEqual(NandGate.nand(1, 1), 0)

class TestNot(unittest.TestCase):
    def test_compute(self):
        not_gate = Not()
        self.assertEqual(not_gate.compute([0]), [1])
        self.assertEqual(not_gate.compute([1]), [0])

class TestAnd(unittest.TestCase):
    def test_compute(self):
        and_gate = And()
        self.assertEqual(and_gate.compute([0, 0]), [0])
        self.assertEqual(and_gate.compute([0, 1]), [0])
        self.assertEqual(and_gate.compute([1, 0]), [0])
        self.assertEqual(and_gate.compute([1, 1]), [1])

class TestOr(unittest.TestCase):
    def test_compute(self):
        or_gate = Or()
        self.assertEqual(or_gate.compute([0, 0]), [0])
        self.assertEqual(or_gate.compute([0, 1]), [1])
        self.assertEqual(or_gate.compute([1, 0]), [1])
        self.assertEqual(or_gate.compute([1, 1]), [1])

if __name__ == "__main__":
    unittest.main()
