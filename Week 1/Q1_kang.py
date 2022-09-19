n = int(input())
list = map(int, input().split())
list = sorted(list)
count = 0
group = []
for i in list:
    group.append(i)
    if len(group) == max(group):
        count += 1
        group = []

print(count)
