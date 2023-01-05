
n = int(input())
home = list(map(int, input().split()))

# full search
# def setting(data):
#     return data[1]
# len = [[i, 0] for i in range(100001)]
# for i in range(1, 100001):
#     len[i][1] = (sum([abs(h-i) for h in home]))
# print(sorted(len[1:], key=setting)[0][0])


# 중앙값에 위치하면 최적의 장소 찾을 수 있음

print(sorted(home)[(n-1)//2])