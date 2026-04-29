# 2606_바이러스 
# 입력 방식: 양뱡향 tree(graph)


N = int(input())
E = int(input())
tree=[[] for _ in range(N+1)]
for _ in range(E):
    u ,v = map(int,input().split())
    tree[u].append(v)
    tree[v].append(u)

# dfs
visited = [False]*(N+1)
count = 0 # count variable 
def dfs(v):
    global count
    visited[v] = True
    count += 1
    for i in tree[v]:
        if not visited[i]:
            dfs(i)
dfs(1)
print(count-1)