# CODE CHALLENGE: Solve the Overlap Alignment Problem.
# Find a highest-scoring alignment between two strings.
# Input: A match score ms, a mismatch penalty mp, a gap penalty gp, and two DNA strings s1 and s2.
# Output: The maximum alignment score of s1 and s2 followed by an alignment achieving this maximum score.

import unittest

from global_alignment import alignment_helper
from fitting_alignment import backtracked_sequence  

def overlap_alignment(ms, mp, gp, s1_suff, s2_pref):
  '''Returns the overlap alignment of strings s1 (shorter or equal) and s2 with match score ms, 
  mismatch penalty mp and gap penalty gp.'''
  
  cache, backtracking_pointers = alignment_helper(ms, mp, gp, s1_suff, s2_pref, localy = True)
  cache = cache[:, len(s1_suff)]
  start_row = cache.argmax()
  alignments = backtracked_sequence(backtracking_pointers, s1_suff, s2_pref, start_row, len(s1_suff)) 
  return cache[start_row], alignments[0], alignments[1]


class TestOverAlign(unittest.TestCase):

  def test_overlap_alignment(self):
    
    # a small example (with many possible alignments):
    self.assertEqual(overlap_alignment(1, 1, 2, 'GAGA', 'GAT'), (2, 'GA', 'GA') )
    
    self.assertEqual(overlap_alignment(1, 1, 1, 'CCAT', 'AT'), (2, 'AT', 'AT'), 
                     "Problem with the backtracking routine or the segment table inproperly initialized.")
    
    self.assertEqual(overlap_alignment(1, 5, 1, 'GAT', 'CAT'), (1, '-AT', 'CAT'), 
                     "The segment table incorrectly penalizing indels in the string s1.")
    
    # len(string1) << len(string2)
    self.assertEqual(overlap_alignment(2, 1, 1, 'CTT', 'AGCATAAAGCATT'), 
                     (1, '--CTT', 'AGCAT'), 
                     "Case len(string1) << len(string2) is not handled correctly.")
    
    # len(string1) >> len(string2)
    self.assertEqual(overlap_alignment(3, 2, 2, 'CAGAGATGGCCG', 'ACG'), 
                     (4, '-CG', 'ACG'),
                     "Case len(string1) >> len(string2) is not handled correctly.")
    
    self.assertEqual(overlap_alignment(1, 1, 5, 'ATCACTG', 'ATGT'), (1, 'CTG', 'ATG'),
                     "Only the prefix of string s2 must be aligned, not the whole string.")
        
    self.assertEqual(overlap_alignment(1, 5, 1, 'ATCACT', 'AT'), (1, 'ACT', 'A-T'),
                     "You're probably doing global, local or fitting alignment instead.")
    
    
if __name__ == '__main__':
  unittest.main(exit = False)