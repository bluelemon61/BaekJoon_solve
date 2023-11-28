import sys
import heapq

def main():
  N = int(sys.stdin.readline())
  input_list = list(map(int, sys.stdin.readline().split()))
  heap = []
  for num in input_list:
    heapq.heappush(heap, num)
  rank = 0
  rank_list = dict()
  while len(heap):
    num = heapq.heappop(heap)
    rank = rank_list.setdefault(num, rank) + 1
  for num in input_list:
    print(rank_list[num], end=" ")



main()