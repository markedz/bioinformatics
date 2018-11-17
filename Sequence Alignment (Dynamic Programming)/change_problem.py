# CODE CHALLENGE: Solve the Change Problem.
# Input: An non-negative integer money and a non-empty integer array of coin types (coin1, ..., coind).
# Output: The minimum number of coins with denominations coins that changes money.  

import unittest

def change(money, coins): 
  '''Returns the minimal number of coins in the Change Problem. '''
  assert money >= 0 and len(coins) > 0
  
  cache = {0: 0}
  coins = set(coins) #so the 'in' operator takes const time (large problem optimization)
  types_used = set() #types of coins used
  for m in range(1, money + 1):
    if m in coins:
      types_used.add(m)
    cache[m] = min( (cache[m - coin] + 1 for coin in types_used) )
  return cache[money]