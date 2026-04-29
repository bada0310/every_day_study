T = int(input())
for tc in range(1,T+1):
    costs = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    dp  = [0]*(len(arr)+1)
    dp[0] = 0 # 초기값
    
    for i in range(1,13):
        curr_val = min(arr[i-1]*costs[0], costs[1]) # day -1month
        
        dp[i] = dp[i-1] + curr_val
        
        if i >= 3:
            dp[i] = min(dp[i], dp[i-3] + costs[2])# 1month -3month
    
    ans = min(dp[12], costs[3])
    print(f'#{tc}',ans)
            
