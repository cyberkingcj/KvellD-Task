import unittest
from agent import Agent

class TestAgent(unittest.TestCase):
    
    def setUp(self):
        self.agent = Agent()
    
    def test_basic_arithmetic(self):
        # test the example from requirements
        result, _ = self.agent.execute("Add 1 and 1, then multiply with 10, then subtract 0.5 from it, and add 4.")
        self.assertEqual(result, 23.5)
    
    def test_division(self):
        result, _ = self.agent.execute("Add 5 and 3, then divide by 2")
        self.assertEqual(result, 4.0)
    
    def test_complex_chain(self):
        result, _ = self.agent.execute("Multiply 7 and 6, then subtract 10, then add 3")
        self.assertEqual(result, 35.0)
    
    def test_division_by_zero(self):
        # should raise an error
        with self.assertRaises(RuntimeError):
            self.agent.execute("Add 5 and 5, then divide by 0")
    
    def test_invalid_query(self):
        with self.assertRaises(ValueError):
            self.agent.execute("do something random")

if __name__ == '__main__':
    unittest.main()
