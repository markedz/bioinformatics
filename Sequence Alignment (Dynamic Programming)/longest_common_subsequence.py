# CODE CHALLENGE: Solve the Longest Common Subsequence Problem.
# Input: Two strings string1 and string2, both with at least one character.
# Output: A longest common subsequence of string1 and string2
# Note: If more than one LCS exists, you may return any one.

import unittest
import numpy as np
import operator

def backtracked_sequence(backtr_ptrs, s1, s2, n, m):
  '''Restores the longest common subsequence of string s11 and string s2 based on
  directions in the backtr_ptrs list. Directions should be encoded as integers
  in the following way: 0 = "down", 1 = "right", 2 = "diagonal".'''
  
  lcs = []
  i, j = n, m
  while i != 0 and j != 0:
    if backtr_ptrs[i-1, j-1] == 0:
      i -= 1
    elif backtr_ptrs[i-1, j-1] == 1:
      j -= 1
    else:
      assert s1[i-1] == s2[j-1] # LCS specific condition
      lcs.append(s1[i-1])
      i -= 1; j -= 1
  return ''.join(lcs[::-1])  

def lcs(string1, string2):
  '''Returns the longest common subsequence of string1 and string2.'''
  
  n = len(string1)
  m = len(string2)
  
  cache = np.zeros((n + 1, m + 1), dtype = np.int)
  backtracking_pointers = np.zeros((n, m), dtype = np.int)
  
  for i in range(1, n + 1):
    for j in range(1, m + 1):
      #0 = "down", 1 = "right", 2 = "diag"
      backtracking_pointers[i-1, j-1], cache[i, j] = max(
      enumerate([
      cache[i-1, j], 
      cache[i, j-1],
      cache[i-1, j-1] + int(string1[i-1] == string2[j-1])]),
      key = operator.itemgetter(1))
  return backtracked_sequence(backtracking_pointers, string1, string2, n, m) 


class TestLcs(unittest.TestCase):

  def test_lcs(self):
    
    #a small example:
    self.assertEqual(lcs('GACT', 'ATG'), 'AT')
    
    #a simple backtracking check:
    self.assertEqual(lcs('AC', 'AC'), 'AC', "Problem with the backtracking routine.")
    
    # len(string1) > len(string2)
    self.assertEqual(lcs('GGTGACGT', 'CT'), 'CT', "Case len(string1) > len(string2) is not handled correctly.")
    
    # len(string1) < len(string2)
    self.assertEqual(lcs('AA', 'CGTGGAT'), 'A', "Case len(string1) < len(string2) is not handled correctly.")
    
    #optimality check:
    self.assertEqual(lcs('ACTGAG', 'GACTGG'), 'ACTGG', "You probably solved the longest common substring problem \
                                             with output ACTG, instead of the longest common subsequence problem.")

    #Boundary cases:
    self.assertEqual(lcs('A', 'T'), '', "Empty result case not handled properly.")
        
    self.assertEqual(lcs('GGGGT', 'CCCCT'), 'T',
                     "Off-by-one error when considering the ends of both strings.")
    
    self.assertEqual(lcs('TCCCC', 'TGGGG'), 'T',
                     "Off-by-one error when considering the beginnings of both strings.")
    
if __name__ == '__main__':
  unittest.main(exit = False)