# CODE CHALLENGE: Solve the Local Alignment Problem (the Smith-Waterman algorithm).
# Find a highest-scoring alignment between two strings.
# Input: A match score ms, a mismatch penalty mp, a gap penalty gp, and two DNA strings s1 and s2.
# Output: The maximum alignment score of s1 and s2 followed by an alignment achieving this maximum score.

import unittest
import numpy as np

from global_alignment import alignment_helper
from global_alignment import backtracked_sequence 

def local_alignment(ms, mp, gp, s1, s2):
  '''Returns the local alignment of strings s1 and s2 with match score ms, 
  mismatch penalty mp and gap penalty gp.'''
  assert gp >= 0
  
  cache, backtracking_pointers = alignment_helper(ms, mp, gp, s1, s2, localy = True, localx = True)
  start_point = np.unravel_index(cache.argmax(), cache.shape)
  alignments = backtracked_sequence(backtracking_pointers, s1, s2, start_point[0], start_point[1], local = True) 
  return cache[start_point[0], start_point[1]], alignments[0], alignments[1]


class TestLocAlign(unittest.TestCase):

  def test_local_alignment(self):
    
    # a small example:
    self.assertEqual(local_alignment(1, 1, 2, 'GAGA', 'GAT'), (2, 'GA', 'GA') )
    
    # a simple backtracking check:
    self.assertEqual(local_alignment(1, 1, 2, 'AC', 'AC'), (2, 'AC', 'AC'), 
                     "Problem with the backtracking routine.")
    
    # optimality and larger backtracking check:
    self.assertEqual(local_alignment(1, 1, 1, 'TAACG', 'ACGTG'), (3, 'ACG', 'ACG'),
                     "Not optimal solution or error in the backtracking routine.")
    
    # len(string1) >> len(string2).
    self.assertEqual(local_alignment(3, 2, 1, 'CAGAGATGGCCG', 'ACG'), (6, 'CG', 'CG'),
                     "Case len(string1) >> len(string2) is not handled correctly.")
    
    # len(string1) << len(string2)
    self.assertEqual(local_alignment(2, 3, 1, 'CTT', 'AGCATAAAGCATT'), (5, 'C-TT', 'CATT'), 
                     "Case len(string1) << len(string2) is not handled correctly.")
    
    self.assertEqual(local_alignment(3, 3, 1, 'AGC', 'ATC'), (4, 'AG-C', 'A-TC'),
                     "Mismatch and gap penalty are incorrectly applied.")
        
    self.assertEqual(local_alignment(1, 1, 1, 'AT', 'AG'), (1, 'A', 'A'),
                     "Mismatch penalty is incorrectly applied.")
    
    
    
if __name__ == '__main__':
  unittest.main(exit = False)