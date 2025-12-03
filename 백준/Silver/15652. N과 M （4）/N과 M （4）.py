N, M = map(int, input().split())

def seq(start, depth, pick):
    if depth == M:
        print(*pick)
        return
    for i in range(start, N+1):
        seq(i, depth+1, pick + [i])
seq(1, 0, [])