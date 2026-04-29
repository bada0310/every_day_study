def dfs(idx,curr_sum):
    global cnt 
    if curr_sum > K: # pruning
        return
    if idx == N:
        if curr_sum == K:
            cnt += 1
        return
    dfs(idx+1, curr_sum + arr[idx])
    dfs(idx+1,curr_sum)
    
T= int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    arr = list(map(int,input().split()))
    cnt = 0
    dfs(0,0)
    print(f'#{tc}',cnt)