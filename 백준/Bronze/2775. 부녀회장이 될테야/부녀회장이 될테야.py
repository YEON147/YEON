T = int(input())
for tc in range(T):
    k = int(input())
    n = int(input())
    A = [[0] * n for _ in range(k+1)]

    for j in range(1, n+1):
        A[0][j-1] = j

    for i in range(1, k+1):
        for j in range(n):
            A[i][j] = A[i-1][j] + A[i][j-1]

    print(A[k][n-1])