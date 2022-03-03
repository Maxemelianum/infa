
with open('zadanie24_2.txt') as file:
    s = file.readline()

s = s.replace('LDR', 'M')
count = max_count = 0
for i in range(len(s)):
    if s[i] == 'M':
        count += 3
    else:
        if count > 0 and s[i+1] == 'L':
            count += 1
            if s[i+2] == 'D':
                count += 1
        max_count = max(count, max_count)
        count = 0

print(max_count)