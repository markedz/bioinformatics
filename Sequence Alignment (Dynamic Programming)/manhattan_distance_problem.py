# CODE CHALLENGE: Find the length of a longest path in the Manhattan Tourist Problem.
# Input: Integers n and m, followed by an n x (m + 1) matrix down and an (n + 1) x m matrix right.
# The two matrices are separated by the - symbol.
# Output: The length of a longest path from source (0, 0) to sink (n, m) in the n x m rectangular grid whose
# edges are defined by the matrices down and right.

import unittest
import numpy as np

def manhattan(n, m, weights_down, weights_right):
  '''Returns the length of a longest path in the Manhattan Tourist Problem.'''
  assert len(weights_down) == n*(m + 1)
  assert len(weights_right) == m*(n + 1)
  
  cache = np.zeros( (n + 1,m + 1), dtype = np.float64)
  weights_down = np.array(weights_down, dtype = np.float64).reshape(n, m + 1)
  weights_right = np.array(weights_right, dtype = np.float64).reshape(n + 1, m)
  
  cache[1:, 0] = np.cumsum(weights_down[:, 0])
  cache[0, 1:] = np.cumsum(weights_right[0, :])
  
  for i in range(1, n + 1):
    for j in range(1, m + 1):
      cache[i, j] = max(cache[i - 1, j] + weights_down[i - 1, j], 
                        cache[i, j - 1] + weights_right[i, j - 1])
      
  return cache[n, m]

class TestManhattan(unittest.TestCase):

  def test_manhattan(self):
    
    #a small example:
    self.assertEqual(manhattan(1, 1, '1 0'.split(), 
                            '1 1'.split() ), 2)
    
    #a larger example:
    self.assertEqual(manhattan(4, 4, '1 0 2 4 3 4 6 5 2 1 4 4 5 2 1 5 6 8 5 3'.split(), 
                            '3 2 4 0 3 2 4 2 0 7 3 3 3 3 0 2 1 3 2 2'.split() ), 34)
    
    # n > m
    self.assertEqual(manhattan(5, 3, '20 5 0 10 0 5 10 0 10 10 0 15 0 20 20 25 30 10 5 30'.split(),
                            '0 30 15 10 20 10 10 10 20 20 25 30 15 35 40 15 10 25'.split() ), 175, 
                            "Case n > m is not handled correctly.")
    
    # n < m
    self.assertEqual(manhattan(3, 5, '0 5 10 0 10 10 15 0 20 20 25 30 10 5 30 15 0 20'.split(),
                            '0 30 15 10 20 10 10 10 20 20 25 30 15 35 40 15 10 25 15 20'.split() ), 180, 
                            "Case n < m is not handled correctly.")
    
    #optimality check:
    self.assertEqual(manhattan(2, 2, [20, 0, 0, 0, 0, 0], [0, 30, 0, 0, 0, 0]), 30,
                     "You used the greedy algorithm instead of dynamic programming")

    #Boundary cases:
    self.assertEqual(manhattan(2, 0, [1, 1], []), 2, "m = 0 case not handled correctly")
    
    self.assertEqual(manhattan(0, 2, [], [1, 1]), 2, "n = 0 case not handled correctly")
    
    self.assertEqual(manhattan(2, 2, [20, 0, 0, 20, 0, 0], [0, 0, 0, 0, 10, 10]), 60,
                     "Off-by-one error when considering the weight matrix.")
    
    self.assertEqual(manhattan(2, 2, [0, 0, 20, 0, 0, 20], [10, 10, 0, 0, 0, 0]), 60,
                     "Off-by-one error when considering the weight matrix.")
    
if __name__ == '__main__':
  unittest.main(exit = False) 