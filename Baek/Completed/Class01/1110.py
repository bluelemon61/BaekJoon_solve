initial = int(input())
num = initial
num2 = -1
count = 0

while initial != num2:
    num = ((num % 10) * 10) + ((int(num / 10) + (num % 10)) % 10)
    num2 = num
    count += 1

print(count)