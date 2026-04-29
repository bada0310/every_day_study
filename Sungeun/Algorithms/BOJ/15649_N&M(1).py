N, M = map(int,input().split())
arr = [i for i in range(1,N+1)]
# 순열(dfs)
visited = [False]*N
result = []

def dfs(depth): # depth 현재 뽑은 갯수 
    
    if depth == M: # 길이가 같아지면 
        print(*result)
        return  
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            result.append(arr[i])
            
            dfs(depth+ 1)
            result.pop()
            visited[i] =False

dfs(0)

                
