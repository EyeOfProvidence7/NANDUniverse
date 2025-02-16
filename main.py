from nand_components import *

nand_gate = NandGate()

not_gate = Not(nand_gate=nand_gate)

print("NOT(0):", not_gate.compute([0])) 

print("NAND Gate call count after NOT gate computations:", nand_gate.call_count)