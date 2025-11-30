N = int(input())

N2 = N // 2 + 1
length = 0
found = False
ans = []

while not found:
    li = [N, N2]
    idx = 2
    while True:
        new = li[idx-2] - li[idx-1]
        if new < 0:
            if len(li) >= length:
                length = len(li)
                N2 += 1
                ans = li
            else:
                found = True
                print(length)
                print(*ans)
            break
        li.append(new)
        idx += 1