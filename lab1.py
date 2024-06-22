def num_jewels_in_stones(jewels, stones):
  jewel_set = set(jewels)
  return sum(stone in jewel_set for stone in stones)
jewels = "aA"
stones = "aAAbbbb"
num_of_jewels = num_jewels_in_stones(jewels, stones)
print(num_of_jewels)  
jewels = "z"
stones = "ZZ"
num_of_jewels = num_jewels_in_stones(jewels, stones)
print(num_of_jewels)  