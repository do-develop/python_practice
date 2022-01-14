def edit_dist(str1, str2):
    r = len(str1)
    c = len(str2)

    dp = [[0]*(c+1) for _ in range(r+1)]

    for i in range(1, r + 1):
        dp[i][0] = i
    for j in range(1, c + 1):
        dp[0][j] = j

    for i in range(1, r + 1):
        for j in range(1, c + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1],
                                   dp[i-1][j],
                                   dp[i-1][j-1])
    return dp[r][c]

str1 = input()
str2 = input()

print(edit_dist(str1, str2))
            
