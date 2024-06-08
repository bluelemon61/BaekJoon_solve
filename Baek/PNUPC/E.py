import sys

N = int(sys.stdin.readline())
tree = [{'ball': False, 'total': 0} for _ in range(2**N)]
tree_b = [0 for _ in range(2**N)]

# 비어있는곳
# 양쪽이 비어있으면 공이 더 적은 쪽
# 양쪽이 비어있고 공 개수가 같으면 홀->오 짝->왼

Q = int(sys.stdin.readline())
for q in range(Q):
  now = 2**N
  for i in range(int(sys.stdin.readline())-1):
    for n in range(N):
      now = now//2