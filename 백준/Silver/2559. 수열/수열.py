N, K = map(int, input().split())
num = list(map(int, input().split()))
S = sum(num[:K])
maxi = S
for i in range(K, N):
    S -= num[i-K]
    S += num[i]
    maxi = max(maxi, S)
print(maxi)