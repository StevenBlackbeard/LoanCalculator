import math

x = int(input())
print(round(math.exp(x) / (math.exp(x) + 1), 2))
# print(round(1 / (1 + math.exp(-x)), 2))