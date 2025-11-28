N, M = map(int, input().split())
pick = [0]* (N+1)

def comb(new:list):
    if len(new) == M:
        print(*new)
        return 
    for i in range(1, N+1):
        if not pick[i]:
            pick[i] = 1
            new.append(i)
            comb(new)
            new.pop()
            pick[i] = 0
comb([])