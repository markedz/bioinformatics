# CODE CHALLENGE: Find the edit distance between two strings.
# Input: Strings s1 and s2.
# Output: The edit distance between s1 and s2.

import unittest
import numpy as np

from global_alignment import alignment_helper

def edit_distance(s1, s2):
  '''Returns the edit distance of strings s1 and s2.'''
  
  cache, _ = alignment_helper(0, 1, 1, s1, s2)
  return -cache[len(s2), len(s1)]


class TestEdDist(unittest.TestCase):

  def test_edit_distance(self):
    
    # small examples:
    self.assertEqual(edit_distance('GACT', 'ATG'), 3 )
    
    self.assertEqual(edit_distance('GAGA', 'GAT'), 2 )
    
    self.assertEqual(edit_distance('AC', 'AC'), 0,
                     "Exactly matching strings incorrectly handled.")
    
    # len(string1) >> len(string2).
    self.assertEqual(edit_distance('CAGACCGAGTTAG', 'CGG'),10,
                     "Case len(string1) >> len(string2) incorrectly handled.")
    
    # len(string1) << len(string2)
    self.assertEqual(edit_distance('CGT', 'CAGACGGTGACG'), 9, 
                     "Case len(string1) << len(string2) incorrectly handled.")
    
    self.assertEqual(edit_distance('AT', 'G'), 2,
                     "Deletions or substitutions are incorrectly handled.")
    
    
if __name__ == '__main__':
  unittest.main(exit = False)