N = int(input())
bulb = list(map(int, input().split()))
S = int(input())

for student in range(S):
    xy, num = map(int, input().split())
    if xy == 1:
        for idx in range(N):
            if (idx+1)%num == 0:
                bulb[idx] = 1-bulb[idx]
    elif xy == 2:
        l = r = 0
        while num-1-l >= 0 and num-1+r < N and bulb[num-1-l] == bulb[num-1+r]:
            l += 1
            r += 1
        l -= 1
        r -= 1
        for o in range(num-1-l, num-1+r+1):
            bulb[o] = 1-bulb[o]

for i in range(0, N, 20):
    print(*bulb[i:i+20])