#Frequent Words with Mismatches and Reverse Complements Problem: Find the most frequent k-mers (with mismatches and reverse complements) in a DNA string.
#      Input: A DNA string Text as well as integers k and d.
#      Output: All k-mers Pattern maximizing the sum Countd(Text, Pattern) + Countd(Text, complement(Pattern))
#      over all possible k-mers.  

import unittest

from most_frequent_words_with_mismatches import compile_dna

def reverse_complement(dna):
  compl = []
  for base in dna:
    if base == 'A':
      compl.append('T')
    elif base == 'T':
      compl.append('A')
    elif base == 'C':
      compl.append('G')
    elif base == 'G':
      compl.append('C')
  return ''.join(compl[::-1])  
  
def most_freq_kmers_mismatch_complement(dna, k, d):
  '''Returns a list of most frequent k-mers with up to d mismatches in the input dna and its reverse complement. '''
  assert len(dna) >= k, "k should be at least the length of dna."
  
  hist1 = compile_dna(dna, k, d)
  hist2 = compile_dna(reverse_complement(dna), k, d)
  
  for kmer in hist2:
    hist1[kmer] = hist1.get(kmer, 0) + hist2[kmer]
    
  max_freq = max(hist1.values())
  return [kmer for kmer in hist1 if hist1[kmer]==max_freq]

class TestMostFreqKmersMismatchRevCompl(unittest.TestCase):

  def test_most_freq_kmers_mismatch_complement(self):
    
    #a small example:
    self.assertItemsEqual(most_freq_kmers_mismatch_complement('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4, 1), 
                          ['ACAT', 'ATGT']) 
                          
                          
    self.assertItemsEqual(most_freq_kmers_mismatch_complement('AGTCAGTC', 4, 2), 
                          ['AATT', 'GGCC'], 
                          "Don't swap d and k.")
    
    #Boundary cases:
    # d = 0
    self.assertItemsEqual(most_freq_kmers_mismatch_complement('AAT', 3, 0), 
                          ['AAT', 'ATT'], 
                          "Please include matches with reverse complement of dna.")
    self.assertItemsEqual(most_freq_kmers_mismatch_complement('AATTAATTGGTAGGTAGGTA', 4, 0), 
                          ['AATT'], 
                          "Please include matches with reverse complement of dna.")
    
    # k = len(dna)
    self.assertItemsEqual(most_freq_kmers_mismatch_complement('ATA', 3, 1), 
                          'AAA AAT ACA AGA ATA ATC ATG ATT CAT CTA GAT GTA TAA TAC TAG TAT TCT TGT TTA TTT'.split(),
                          "Not enough kmers in output.")
    
    # dna formed from a single base
    self.assertItemsEqual(most_freq_kmers_mismatch_complement('AAAAAAAAAA', 2, 1), 
                          ['AT', 'TA'], 
                          "d > 0 allows non-exact matches that don't appear in the given dna.")
    
    # d > k
    self.assertItemsEqual(most_freq_kmers_mismatch_complement('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4, 12), 
                          most_freq_kmers_mismatch_complement('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4, 4),
                          "Case d > k not handled properly.")
    
if __name__ == '__main__':
    unittest.main(exit = False)