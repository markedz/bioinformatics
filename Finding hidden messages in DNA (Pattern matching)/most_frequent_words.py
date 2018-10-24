#Frequent Words Problem: Find the most frequent k-mers in a string.
#(k-mer is a string of length k)
#     Input: A string Text and an integer k.
#     Output: All most frequent k-mers in Text.

import unittest

def compile_text(string, k):
  '''Returns a counter of words of length k in the input string.'''
  
  histogram = {}
  kmers = len(string)-k+1
  for i in range(kmers):
    kmer = string[i:(i+k)]
    histogram[kmer] = histogram.get(kmer, 0) + 1
  return histogram

def most_freq_kmers(string, k):
  '''Returns a list of most frequent k-mers in the input string'''
  assert len(dna) >= k, "k should be at least the length of dna."
  
  hist = compile_text(string, k)
  max_freq = max(hist.values())
  return [kmer for kmer in hist if hist[kmer]==max_freq] 


class TestMostFreqKmers(unittest.TestCase):

  def test_most_freq_kmers(self):
    
    #a small example:
    self.assertItemsEqual(most_freq_kmers('ATATA', 2), ['AT', 'TA'])
    #Python3:
    #self.assertCountEqual(most_freq_kmers('ATATA', 2), ['AT', 'TA'])
    
    #a larger example:
    self.assertItemsEqual(most_freq_kmers('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4), ['CATG', 'GCAT'])
    
    #Boundary cases for larger strings
    self.assertItemsEqual(
      most_freq_kmers( 
      'TGGTAGCGACGTTGGTCCCGCCGCTTGAGAATCTGGATGAACATAAGCTCCCACTTGGCTTATTCAGAGAACTGGTCAACACTTGTCTCTCCCAGCCAGGTCTGACCACCGGGCAACTTTTAGAGCACTATCGTGGTACAAATAATGCTGCCAC', 
      3), ['TGG'], "First kmer not counted!")
  
    self.assertItemsEqual(
      most_freq_kmers( 
      'CAGTGGCAGATGACATTTTGCTGGTCGACTGGTTACAACAACGCCTGGGGCTTTTGAGCAACGAGACTTTTCAATGTTGCACCGTTTGCTGCATGATATTGAAAACAATATCACCAAATAAATAACGCCTTAGTAAGTAGCTTTT',
      4), ['TTTT'], "Last kmer not counted!")
    
    self.assertItemsEqual(
      most_freq_kmers( 
      'ATACAATTACAGTCTGGAACCGGATGAACTGGCCGCAGGTTAACAACAGAGTTGCCAGGCACTGCCGCTGACCAGCAACAACAACAATGACTTTGACGCGAAGGGGATGGCATGAGCGAACTGATCGTCAGCCGTCAGCAACGAGTATTGTTGCTGACCCTTAACAATCCCGCCGCACGTAATGCGCTAACTAATGCCCTGCTG',
      5), ['AACAA'], "Overlapping occurrences not counted properly!")

if __name__ == '__main__':
    unittest.main(exit = False)