[n, m] = list(map(int, input().split(' ')))
cards = list(map(int, input().split(' ')))

cards.sort()

result = 0


end = 2
endflag = 0
for i in range(n-2):
    endflag = cards[0] + cards[1] + cards[end]
    end += 1
    if endflag > m:
        break

for first in range(end-2):
    for second in range(first+1, end-1):
        for third in range(second+1, end):
            sum_card = cards[first] + cards[second] + cards[third]
            if sum_card <= m and sum_card > result:
                result = sum_card
            if result == m:
                break
        if result == m:
                break
    if result == m:
                break

print(result)