#Approximate Pattern Matching Problem: Find all approximate occurrences of a pattern in a string.
#     Input: Two strings Pattern and Text along with an integer d.
#     Output: All positions where Pattern appears in Text with at most d mismatches.

import unittest

def similar(string1, string2, d): 
  '''Checks whether two strings are the same up to at most d mismatches.'''
  assert len(string1) == len(string2)
  
  mismatch_count = 0
  for i in range(len(string1)):
    if string1[i] != string2[i]:
      mismatch_count += 1
    if mismatch_count > d:
      return False
  return True

def pattern_match_approx(pattern, dna, d): 
  '''Returns a list of positions in dna where the pattern occurrs approximately  
  (with up to d mismatches). '''
  
  positions = []
  pat_len = len(pattern)
  for i in range(len(dna) - pat_len + 1):
    if similar(pattern, dna[i:(i + pat_len)], d):
      positions.append(i)
  return positions

class TestApproxPatternMatching(unittest.TestCase):

  def test_approx_pattern_matching(self):
    
    #a small example:
    self.assertItemsEqual(pattern_match_approx('ATTCTGGA',
    'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT', 
    3), [6, 7, 26, 27])
    
    self.assertItemsEqual(pattern_match_approx(
    'AAA', 'TTTTTTAAATTTTAAATTTTTT', 
    2), [4, 5, 6, 7, 8, 11, 12, 13, 14, 15], 
    'Should count instances where the number of mismatches is up to d, not exactly d.')
    
    self.assertItemsEqual(pattern_match_approx(
    'TTT', 'AAAAAA', 
    3), [0, 1 ,2, 3], 
    'Should count instances where the number of mismatches is up to d, not less than d.')
    
    #Boundary cases
    self.assertItemsEqual(pattern_match_approx(
    'GC', 'ATA', 1),
    [], 'Case of no matches found is incorrectly handled.')
    
    self.assertItemsEqual(pattern_match_approx(
    'GAGCGCTGG', 'GAGCGCTGGGTTAACTCGCTACTTCCCGACGAGCGCTGTGGCGCAAATTGGCGATGAAACTGCAGAGAGAACTGGTCATCCAACTGAATTCTCCCCGCTATCGCATTTTGATGCGCGCCGCGTCGATT',
    2), [0, 30, 66], 'First kmer not included!')
    
    self.assertItemsEqual(pattern_match_approx(
    'AATCCTTTCA', 'CCAAATCCCCTCATGGCATGCATTCCCGCAGTATTTAATCCTTTCATTCTGCATATAAGTAGTGAAGGTATAGAAACCCGTTCAAGCCCGCAGCGGTAAAACCGAGAACCATGATGAATGCACGGCGATTGCGCCATAATCCAAACA',
    3), [3, 36, 74, 137], 'Last kmer not included!')
    
    self.assertItemsEqual(pattern_match_approx(
    'CCGTCATCC', 'CCGTCATCCGTCATCCTCGCCACGTTGGCATGCATTCCGTCATCCCGTCAGGCATACTTCTGCATATAAGTACAAACATCCGTCATGTCAAAGGGAGCCCGCAGCGGTAAAACCGAGAACCATGATGAATGCACGGCGATTGC',
    3), [0, 7, 36, 44, 48, 72, 79, 112], 'Overlapping occurrences not properly accounted for!')
    
if __name__ == '__main__':
    unittest.main(exit = False)    