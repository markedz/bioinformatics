#Pattern Matching Problem: Find all occurrences of a pattern in a string.
#     Input: Two strings, Pattern and Genome.
#     Output: All starting positions where Pattern appears as a substring of Genome.

import unittest

def pattern_matching(pattern, dna):
  '''Returns a list of positions in dna where the pattern occurrs. '''
  
  positions = []
  pos = dna.find(pattern)
  while pos!=-1:
    positions.append(pos)
    pos = dna.find(pattern, pos + 1)
  return positions

class TestPatternMatching(unittest.TestCase):

  def test_pattern_matching(self):
    
    #a small example:
    self.assertItemsEqual(pattern_matching('ATAT', 'GATATATGCATATACTT'), [1, 3, 9])
    
    self.assertItemsEqual(pattern_matching(
    'ACAC', 'TTTTACACTTTTTTGTGTAAAAA'), 
    [4], 'The function should not include reverse complements.')
    
    #Boundary cases
    self.assertItemsEqual(pattern_matching(
    'GT', 'ATA'),
    [], 'Case of no matches found is incorrectly handled.')
    
    self.assertItemsEqual(pattern_matching(
    'AAA', 'AAAGAGTGTCTGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAATTAAATTTTATTGACTTAGGTCACTAAATACTTTAACCAATATAGGCATAGCGCACAGACAGATAATAATTACAGAGTACACAACATCCAT'),
    [0, 46, 51, 74], 'First kmer not included!')
    
    self.assertItemsEqual(pattern_matching(
    'TTT', 'AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT'),
    [88, 92, 98, 132], 'Last kmer not included!')
    
    self.assertItemsEqual(pattern_matching(
    'ATA', 'ATATATA'),
    [0, 2, 4], 'Overlapping occurrences not included!')
    
    
if __name__ == '__main__':
    unittest.main(exit = False)    