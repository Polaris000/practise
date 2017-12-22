# Find the sum of the multiples of 3 or 5 below 1000

d = 0
for i in range(1, 1000):
  if i % 3 == 0 or i % 5 == 0:
    d += i
    
print(d)
