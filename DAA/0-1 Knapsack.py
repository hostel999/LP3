def knapsack_dp():
    val = [50, 100, 150, 200]
    wt = [8, 16, 32, 40]
    W = 64
    n = len(val)
    # DP table where dp[i][w] will hold the max value for first i items with weight <= w
    dp = [[0 for w in range(W + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i-1] <= w:
                dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    print("Maximum value in 0-1 Knapsack =", dp[n][W])

if __name__ == "__main__":
    knapsack_dp()

# def knapsack(val,wt,W):
#     dp = [0]*(W+1)
#     for i in range(len(val)):
#         weight= wt[i]
#         value= val[i]
#         for w in range(W,weight-1,-1):
#             dp[w]= max(dp[w],value+dp[w-weight])
            
#     print("Maximum value (1D DP) =",dp[W])
# val=[50,100,150,200]
# wt=[8,16,32,40] 
# W=64
# knapsack(val,wt,W)
