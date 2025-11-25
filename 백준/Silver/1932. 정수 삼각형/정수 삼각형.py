n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
new = [[arr[0][0]]]+ [[0] * w for w in range(2, n+1)]

for i in range(1, n):
    for j in range(i+1):
        if i == 1:
            new[i][j] = arr[i][j] + arr[0][0]
            continue
        if j == 0:
            new[i][j] = arr[i][j] + new[i-1][j]
            continue
        if i == j :
            new[i][j] = arr[i][j] + new[i-1][j-1]
            continue
        new[i][j] = arr[i][j] + max(new[i-1][j-1], new[i-1][j])

print(max(new[-1]))