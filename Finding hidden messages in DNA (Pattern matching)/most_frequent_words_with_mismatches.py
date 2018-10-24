#Frequent Words with Mismatches Problem: Find the most frequent k-mers with mismatches in a string.
#     Input: A string Text as well as integers k (word length) and d (maximum amount of mismatches). 
#            (You may assume 0 <= k <= 12 and 0 <= d <= 3.)
#     Output: All most frequent k-mers with up to d mismatches in Text.

import unittest
import itertools as it  
import copy 

from most_frequent_words import compile_text

def possible_mutations():
  bases = ["A","C","G","T"]
  d = {}
  for base in bases:
    d[base] = [b for b in bases if base != b]
  return d


def mutated_kmers(kmer_list, d, base_positions, mutation_dict):
  '''Yields all kmers that match the given kmer with EXACTLY d mismatches'''  
  
  for combin in it.combinations(base_positions, d): 
        # a list of lists of possible mutations in the positions given by the combination
        mut = [mutation_dict[kmer_list[i]] for i in combin] 
        temp = kmer_list + [] # so we can mutate the kmer
        for prod in it.product(*mut):    
          for j in range(d): #mutate all selected mismatches
            temp[combin[j]] = prod[j]
          yield ''.join(temp) 
    

def compile_dna(dna, k, d = 0): 
  '''Returns a histogram of k-mer frequencies in dna with up to d mismatches'''
  assert d >= 0, "d should be non-negative."
  
  if d > k: d = k
  
  hist = compile_text(dna, k)

  kmers = hist.keys()
  mutation_dict = possible_mutations() 
  hist_out = copy.deepcopy(hist)
  base_positions = range(k)
  
  for kmer in kmers:
    kmer_list = list(kmer) # to mutate the kmer
    for d_cur in range(1, d + 1):
          for mut_kmer in mutated_kmers(kmer_list, d_cur, base_positions, mutation_dict):
            hist_out[mut_kmer] = hist_out.get(mut_kmer, 0) + hist[kmer]
    
  return hist_out
  
def most_freq_kmers_mismatch(dna, k, d):  
  '''Returns a list of most frequent k-mers with up to d mismatches in the input string/dna. '''
  assert len(dna) >= k, "k should be at least the length of dna."
  
  hist_out = compile_dna(dna, k, d)
  max_freq = max(hist_out.values())
  return [kmer for kmer in hist_out if hist_out[kmer]==max_freq]

class TestMostFreqKmersMismatch(unittest.TestCase):

  def test_most_freq_kmers_mismatch(self):
    
    #a small example:
    self.assertItemsEqual(most_freq_kmers_mismatch('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4, 1), 
                          ['ATGC', 'ATGT', 'GATG']) 
                          
                          
    self.assertItemsEqual(most_freq_kmers_mismatch('AGTCAGTC', 4, 2), 
                          'TCTC CGGC AAGC TGTG GGCC AGGT ATCC ACTG ACAC AGAG ATTA TGAC AATT CGTT GTTC GGTA AGCA CATC'.split(), 
                          "Don't swap d and k.")
    
    #Boundary cases:
    # d = 0
    self.assertItemsEqual(most_freq_kmers_mismatch('AATTAATTGGTAGGTAGGTA', 4, 0), 
                          ['GGTA'], 
                          "Don't include matches with reverse complement of dna.")
    
    # k = len(dna)
    self.assertItemsEqual(most_freq_kmers_mismatch('ATA', 3, 1), 
                          'GTA ACA AAA ATC ATA AGA ATT CTA TTA ATG'.split(),
                          "Not enough kmers in output.")
    
    # dna formed from a single base
    self.assertItemsEqual(most_freq_kmers_mismatch('AAAAAAAAAA', 2, 1), 
                          ['AA', 'AC', 'AG', 'CA', 'AT', 'GA', 'TA'], 
                          "d > 0 allows non-exact matches that don't appear in the given dna.")
    
    # d > k
    self.assertItemsEqual(most_freq_kmers_mismatch('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4, 12), 
                          most_freq_kmers_mismatch('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4, 4),
                          "Case d > k not handled properly.")
    
if __name__ == '__main__':
    unittest.main(exit = False)