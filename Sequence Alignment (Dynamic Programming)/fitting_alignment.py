# CODE CHALLENGE: Solve the Fitting Alignment Problem.
# Find a highest-scoring alignment between two strings.
# Input: A match score ms, a mismatch penalty mp, a gap penalty gp, and two DNA strings s1 and s2.
# Output: The maximum alignment score of s1 and s2 followed by an alignment achieving this maximum score.

import unittest

from global_alignment import alignment_helper

def backtracked_sequence(backtr_ptrs, s1, s2, start_row, start_col, local = False):
  '''Restores the fitting alignment of string1 and string2 based on
  directions in the backtr_ptrs list. Directions should be encoded as integers
  in the following way: 0 = "down", 1 = "right", 2 = "diagonal", 3 = "to the start".'''
  
  align1, align2 = [], []
  i, j = start_row, start_col
  
  while i != 0:
    if backtr_ptrs[i, j] == 0:
      align1.append('-')
      align2.append(s2[i-1])
      i -= 1 # go up
    elif backtr_ptrs[i, j] == 1:
      align1.append(s1[j-1])
      align2.append('-')
      j -= 1 # go left
    elif backtr_ptrs[i, j] == 2:
      align1.append(s1[j-1])
      align2.append(s2[i-1])
      i-= 1; j -= 1 # go diag
    elif local and backtr_ptrs[i, j] == 3:
      i = 0; j = 0 # go to the start
        
  align1.reverse()
  align2.reverse()
  return ''.join(align1),''.join(align2)   

def fitting_alignment(ms, mp, gp, s1, s2):
  '''Returns the fitting alignment of strings s1 (shorter or equal) and s2 with match score ms, 
  mismatch penalty mp and gap penalty gp.'''
  assert len(s1) <= len(s2)
  
  cache, backtracking_pointers = alignment_helper(ms, mp, gp, s2, s1, localy = True)
  cache = cache[len(s1), :]
  start_col = cache.argmax()
  alignments = backtracked_sequence(backtracking_pointers, s2, s1, len(s1), start_col) 
  return cache[start_col], alignments[1], alignments[0]


class TestFitAlign(unittest.TestCase):

  def test_fitting_alignment(self):
    
    # a small example (with many possible alignments):
    self.assertEqual(fitting_alignment(1, 1, 2, 'GAT', 'GAGA'), (1, 'GAT', 'GAG') )
    
    # optimality check:
    self.assertEqual(fitting_alignment(1, 1, 1, 'AT', 'CCAT'), (2, 'AT', 'AT'), 
                     "Problem with the backtracking routine.")
    
    # len(string1) << len(string2)
    self.assertEqual(fitting_alignment(10, 1, 1, 'GG', 'CAAGACTACTATTAG'), 
                     (10, 'G----------G', 'GACTACTATTAG'), 
                     "Case len(string1) << len(string2) is not handled correctly.")
    
    # len(string1) == len(string2)
    self.assertEqual(fitting_alignment(2, 3, 1, 'CGAGAGGTT', 'ACGACAGAG'), 
                     (7, 'CGA--GAGGTT', 'CGACAGAG---'),
                     "Case len(string1) == len(string2) is not handled correctly.")
    
    self.assertEqual(fitting_alignment(1, 5, 1, 'AT', 'CACGTC'), (0, 'AT', 'A-'),
                     "You're probably doing local or global alignment instead.")
        
    self.assertEqual(fitting_alignment(1, 1, 1, 'AT', 'ATCC'), (2, 'AT', 'AT'),
                     "You're probably doing global alignment instead.")
    
    
if __name__ == '__main__':
  unittest.main(exit = False)