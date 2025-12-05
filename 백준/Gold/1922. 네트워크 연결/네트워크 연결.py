import sys
input = sys.stdin.readline
from heapq import heappop, heappush
def prim(s):
    pq = [(0, s)]
    mini = 0
    MST = [0] * (N+1)
    while pq:
        w, n = heappop(pq)
        if not MST[n]:
            mini += w
            MST[n] = 1

            for nxt_w, nxt_n in G[n]:
                heappush(pq, (nxt_w, nxt_n))
    return mini

N = int(input())
M = int(input())
G = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    G[a].append((c, b))
    G[b].append((c, a))

print(prim(1))