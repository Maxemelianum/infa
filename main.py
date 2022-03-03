

with open('zadanie24_1.txt') as file:
    s = file.readline()

s = s.replace('AB', 'M').replace('AC', 'M')
count = max_count = 0
for i in range(len(s)):
    if s[i] == 'M':
        count += 1

    else:
        max_count = max(count, max_count)
        count = 0

print(max_count)