# 13023_ABCDE
N, M = map(int,input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [False]*N

# dfs
def dfs(now, depth):
    if depth == 4:
        return True
    
    visited[now] =True

    for i in graph[now]:
        if not visited[i]:
            if dfs(i,depth+1):
                return True
    visited[now]=False
    return False
ans = 0
for i in range(N):
    if dfs(i,0):
        ans = 1
        break
print(ans)

