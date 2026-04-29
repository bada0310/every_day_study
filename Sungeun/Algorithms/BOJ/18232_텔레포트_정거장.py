# 가는데까지의 최소 시간을 구하자 > bfs
from collections import deque

N, M = map(int,input().split())
S, E = map(int,input().split())
tree = [[] for _ in range(N+1)]
for _ in range(M):
    key, val = map(int,input().split())
    tree[key].append(val)
    tree[val].append(key)

visited = [-1]*(N+1)
count = 0

# while q 안에서 x -1 x +1 이동이 가능해아함 
def bfs(S):
    global count 
    q = deque([S])
    visited[S] = 0
    while q:
        curr_S = q.popleft()
        
        if curr_S == E:
            return visited[curr_S]
        
        next_lst = [curr_S + 1, curr_S -1] + tree[curr_S] # x-1 , x+ 1 로 이동하는걸 풀이
        
    
        for i in next_lst:
            if 1<= i <= N and visited[i] == -1:
                visited[i] = visited[curr_S] + 1
                q.append(i)
    return -1

print(bfs(S))