# 11724_연결요소의 갯수
# 무향 그래프 
N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False]*(N+1)
cnt = 0
from collections import deque
def bfs(v):
    q = deque([v])
    visited[v] = True

    while q:
        cur_v = q.popleft()
        for i in graph[cur_v]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
for i in range(1,N+1):
    if not visited[i]:
        # dfs(i)
        bfs(i)
        cnt += 1
print(cnt)

# def dfs(v):
#     visited[v] = True
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(i)