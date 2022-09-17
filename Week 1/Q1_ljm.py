# 모험가 길드
# n: 모험가 수
# x: 공포도

n = int(input())
print("n: {}".format(n))

x_data = list(map(int, input().split()))
x_data.sort()
print("x_data: {}".format(x_data))

num_group = 0
in_group = 0
for x in x_data:
    in_group += 1
    if in_group >= x:
        num_group += 1
        in_group = 0

print(num_group)