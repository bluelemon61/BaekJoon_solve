import sys

def peopleDistance(person1, person2):
  distance = 0
  for i in range(4):
    if person1[i] != person2[i]:
      distance += 1
  return distance

def threePeopleDistance():
  N = int(sys.stdin.readline())
  mbti = dict()
  input_list = list(sys.stdin.readline().split())
  for kind in input_list:
    mbti.setdefault(kind, 0)
    mbti[kind] += 1
  
  mbti_list = list(mbti.keys())
  max_count = max(mbti.values())
  max_kind = []
  for kind in mbti_list:
    if max_count == mbti[kind]:
      max_kind.append(kind)
  
  if max_count > 2:
    print(0)
  else:
    min_distance = 100
    for i1 in range(len(input_list)-2):
      for i2 in range(i1+1, len(input_list)-1):
        for i3 in range(i2+1, len(input_list)):
          kind1 = input_list[i1]
          kind2 = input_list[i2]
          kind3 = input_list[i3]
          distance = 0
          distance += peopleDistance(kind1, kind2) 
          distance += peopleDistance(kind2, kind3)
          distance += peopleDistance(kind3, kind1)
          if min_distance > distance:
            min_distance = distance
    print(min_distance)


def main():
  T = int(sys.stdin.readline())
  for i in range(T):
    threePeopleDistance()

main()