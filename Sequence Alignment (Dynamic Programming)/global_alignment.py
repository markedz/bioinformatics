# CODE CHALLENGE: Solve the Global Alignment Problem (the Needleman-Wunsch algorithm).
# Find a highest-scoring alignment between two strings.
# Input: A match score ms, a mismatch penalty mp, a gap penalty gp, and two DNA strings s1 and s2.
# Output: The maximum alignment score of s1 and s2 followed by an alignment achieving this maximum score.

import unittest
import numpy as np
import operator

def backtracked_sequence(backtr_ptrs, s1, s2, start_row, start_col, local = False):
  '''Restores the global alignment of string1 and string2 based on
  directions in the backtr_ptrs list. Directions should be encoded as integers
  in the following way: 0 = "down", 1 = "right", 2 = "diagonal, 3 = "to the start"".'''
  
  align1, align2 = [], []
  i, j = start_row, start_col
  
  while i != 0 or j != 0:
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

def alignment_helper(ms, mp, gp, s1, s2, localy = False, localx = False):
  '''Helper function for global and local alignment.
  Returns the segment table and pointers for backtracking.'''
  
  n, m = len(s1), len(s2)
  local = localy and localx
  
  cache = np.zeros((m + 1, n + 1), dtype = np.float)
  backtracking_pointers = np.zeros((m + 1, n + 1), dtype = np.int)
  
  #init
  cache[0, 1:] = np.arange(1, n + 1)*((-gp) if not localy else 0)
  cache[1:, 0] = np.arange(1, m + 1)*((-gp) if not localx else 0)
  backtracking_pointers[0, 1:] = 1 if not localy else 3
  backtracking_pointers[1:, 0] = 0 if not localx else 3
  
  for i in range(1, m + 1):
    for j in range(1, n + 1):
      #0 = "down", 1 = "right", 2 = "diag"
      backtracking_pointers[i, j], cache[i, j] = max(
      enumerate((
      cache[i-1, j] - gp,
      cache[i, j-1] - gp,
      cache[i-1, j-1] + (ms if s1[j-1]==s2[i-1] else -mp) )),
      key = operator.itemgetter(1))
      
      if local and cache[i, j] <= 0: # to reuse the same code for local alignment
        cache[i, j] = 0
        backtracking_pointers[i, j] = 3
        
  return cache, backtracking_pointers

def global_alignment(ms, mp, gp, s1, s2):
  '''Returns the global alignment of strings s1 and s2 with match score ms, 
  mismatch penalty mp and gap penalty gp.'''
  
  cache, backtracking_pointers = alignment_helper(ms, mp, gp, s1, s2)
  alignments = backtracked_sequence(backtracking_pointers, s1, s2, len(s2), len(s1)) 
  return cache[len(s2), len(s1)], alignments[0], alignments[1]


class TestGlobAlign(unittest.TestCase):

  def test_global_alignment(self):
    
    #a small example (with many possible alignments):
    self.assertEqual(global_alignment(1, 1, 2, 'GAGA', 'GAT')[0], -1 )
    
    #a simple backtracking check:
    self.assertEqual(global_alignment(1, 1, 2, 'AC', 'AC'), (2, 'AC', 'AC'), "Problem with the backtracking routine.")
    
    ## len(string1) >> len(string2).
    self.assertEqual(global_alignment(2, 3, 2, 'ACAGATTAG', 'T'), (-14, 'ACAGATTAG', '-----T---'),
                     "Case len(string1) >> len(string2) is not handled correctly.")
    
    ## len(string1) << len(string2)
    self.assertEqual(global_alignment(3, 1, 2, 'G', 'ACATACGAT'), (-13, '------G--', 'ACATACGAT'), 
                     "Case len(string1) << len(string2) is not handled correctly.")
    
    self.assertEqual(global_alignment(1, 1, 1, 'AT', 'AG'), (0, 'AT', 'AG'),
                     "Mismatch penalty is incorrectly applied.")
        
    self.assertEqual(global_alignment(2, 5, 1, 'TCA', 'CA'), (3, 'TCA', '-CA'),
                     "Make sure your code allows for an output beginning with an indel.")
    
    self.assertEqual(global_alignment(1, 10, 1, 'TTTTCCTT', 'CC'), (-4, 'TTTTCCTT', '----CC--'),
                     "Make sure your code can handle multiple indels in a row.")
    
if __name__ == '__main__':
  unittest.main(exit = False)