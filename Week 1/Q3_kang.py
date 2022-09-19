string = input()
count_zero = 0
count_one = 0

check = 0
while True:
    if check == len(string) -1 :
        break
    if string[check] != string[check+1]:
        if string[check] == '0':
            count_zero += 1
        else:
            count_one += 1

    check += 1
print(min([count_zero, count_one]))