import sys

n = int(sys.stdin.readline())

def fourSquare(n):
  n_sqrt = n ** 0.5
  if n_sqrt % 1 == 0:
    return 1
  
  for i in range(1, int(n_sqrt) + 1):
    i_sqrt = (n - i**2)**0.5
    if i_sqrt % 1 == 0:
      return 2
    
  for i in range(1, int(n_sqrt) + 1):
    i_sqrt = (n - i**2)**0.5
    for j in range(1, int(i_sqrt) + 1):
      j_sqrt = (n - i**2 - j**2)**0.5
      if j_sqrt % 1 == 0:
        return 3
      
  return 4
  
print(fourSquare(n))