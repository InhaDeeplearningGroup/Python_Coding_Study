

def prac_7():
    N = input()
    N_len = len(N)

    left_total = 0
    right_total = 0
    for i in range(N_len // 2):
        left_total += int(N[i])

    for i in range(N_len // 2, N_len):
        right_total += int(N[i])

    if left_total == right_total: print("LUCKY")
    else: print("READY")


def prac_10(key, lock):
    answer = False

    def rotate(m, d):
        N = len(m)
        ret = [[0] * N for _ in range(N)]

        if d % 4 == 1:
            for r in range(N):
                for c in range(N):
                    ret[c][N - 1 - r] = m[r][c]
        elif d % 4 == 2:
            for r in range(N):
                for c in range(N):
                    ret[N - 1 - c][N - 1 - r] = m[r][c]
        elif d % 4 == 3:
            for r in range(N):
                for c in range(N):
                    ret[N - 1 - c][r] = m[r][c]
        else:
            for r in range(N):
                for c in range(N):
                    ret[r][c] = m[r][c]

        return ret

    def lock_zp(k, l):
        size = len(k) // 2
        pad_size = len(l) + 2 * size
        padding = [[0] * (pad_size) for _ in range(pad_size)]

        for i in range(len(l)):
            for j in range(len(l)):
                padding[i + (pad_size // 2 - len(l) // 2)][j + (pad_size // 2 - len(l) // 2)] = l[i][j]

        return padding

    def answer_check(lock_padding):
        size = len(key) // 2
        pad_size = len(lock) + 2 * size
        total_sum = 0
        for x in range(len(lock)):
            for y in range(len(lock)):
                if lock_padding[x + (pad_size // 2 - len(lock) // 2)][y + (pad_size // 2 - len(lock) // 2)] != 0:
                    total_sum += 1
        if total_sum == 9: answer = True
        print(lock_padding)
        print(total_sum)

    for rot in range(4):
        key_rotate = rotate(key, rot)
        lock_padding = lock_zp(key, lock)

        size = len(key) // 2
        pad_size = len(lock) + 2 * size
        total_sum = 0

        for h in range(len(lock)):
            for w in range(len(lock)):
                for i in range(len(key_rotate)):
                    for j in range(len(key_rotate)):
                        lock_padding[h + i][w + j] += key_rotate[i][j]
                        total_sum = 0
                        answer_check(lock_padding)
                        lock_padding[h + i][w + j] -= key_rotate[i][j]

    return answer



if __name__ == '__main__':
    prac_10()
