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

if __name__ == "__main__":
    unittest.main()
