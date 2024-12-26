def length_of_lis_dp(arr):
    n = len(arr)
    if n == 0:
        return 0

    dp = [1] * n  # Initialize all LIS lengths to 1

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)  # The length of the LIS
