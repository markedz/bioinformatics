# CODE CHALLENGE: Solve the Change Problem.
# Input: An non-negative integer money and a non-empty integer array of coin types (coin1, ..., coind).
# Output: The minimum number of coins with denominations coins that changes money.  

def change(money, coins, cache = None): 
  '''Returns the minimal number of coins in the Change Problem. '''
  assert money >= 0 and len(coins) > 0

  if cache is None:
    cache = {0 : 0}
    
  if money == 0:
    return cache[money]
  
  coins2use = [coin for coin in coins if coin <= money] 
  if money not in cache:
    cache[money] = min( (change(money - coin, coins2use, cache) + 1 for coin in coins2use) )
  return cache[money]
