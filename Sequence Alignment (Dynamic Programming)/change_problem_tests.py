import unittest

class TestChange(unittest.TestCase):

  def test_change(self):
    
    #a small example:
    self.assertEqual(change(7, [1, 5]), 3)
    
    #optimality check:
    self.assertEqual(change(12, [9, 6, 1]), 2, "You used the greedy algorithm instead of dynamic programming")

    #Boundary cases:
    self.assertEqual(change(10, [1, 2, 3, 4, 5, 10]), 1, "You didn't consider the last coin.")
    
    self.assertEqual(change(11, [1, 5]), 3, "Off-by-one error when considering money variable.")
    
    self.assertEqual(change(0, [1, 5]), 0, "With no money you should get no coins")

if __name__ == '__main__':
  from change_problem import change
  unittest.main(exit = False) 
  from change_problem_recursive import change
  unittest.main(exit = False) 