# 문자열 뒤집기
S = list(map(int, input()))
# print("S: ", S)

num_zero = 0
num_one = 0


for i, num in enumerate(S):
    if i < len(S)-1:
        if S[i] != S[i + 1]:
            if S[i] == 0:
                num_zero += 1
            else:
                num_one += 1

result = min(num_zero, num_one)
print(result)