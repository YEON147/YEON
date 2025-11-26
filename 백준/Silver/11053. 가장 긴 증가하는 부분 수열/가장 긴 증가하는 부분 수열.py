N = int(input())
A = list(map(int, input().split()))

def LIS(arr):
    global N
    dp = [1] * N
    for i in range(N):
        for j in range(i):  
            if arr[j] < arr[i]:
                # j번째까지 증가하는 수열 + 나포함한 수열, 이전에 담아둔 증가하는 수열 중에 max 값
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

print(LIS(A))