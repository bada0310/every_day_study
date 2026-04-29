# 2644 촌수 계산 
from collections import deque
N = int(input())
S, E = map(int,input().split()) # start end 
cmd = int(input()) 
tree = [[] for _ in range(N+1)] # tree input 

for _ in range(cmd):
    key, val = map(int,input().split())
    tree[key].append(val)
    tree[val].append(key) # 양방향 

#bfs? layering 문제 
visited = [0]*(N+1) # 방문 확인용 배열 
def bfs(S):
    q = deque([S])
    visited[S] = 1
    while q:
        curr_S = q.popleft()
        
        if curr_S == E:
            return visited[curr_S] -1
        
        for i in tree[curr_S]:
            if visited[i] == 0:
                visited[i] = visited[curr_S] + 1
                q.append(i)
    return -1

print(bfs(S))