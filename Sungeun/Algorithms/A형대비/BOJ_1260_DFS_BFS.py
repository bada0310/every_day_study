# 1260_DFS& BFS

from collections import deque
# DFS 는 가장 최근에 넣은 노드를 먼저 꺼내야 하므로 stack 을 활용함 
# BFS 는 가장 먼저 넣은 노드를 꺼내야 하므로 Queue 구조를 활용함

def dfs(graph, start_node):
    visited = []
    stack = [start_node]
    # need_visited = deque()

    # 시작 노드 설정해주기 
    # need_visited.append(start_node)
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))
    return visited 

# BFS
def bfs(graph, start_node): 
    visited = [False]*(len(graph)) # 방문 여부를 체크할 리스트 
    que = deque([start_node]) # 숫자를 대괄호로 감싸서 리스트 형태로 만들어야 한다. 
    visited[start_node] = True

    result = [] # 마지막 방문순서가 담긴 list 

    while que:
        node = que.popleft()  # 큐의 맨앞에 들어온 것을 꺼냄
        result.append(node)

        for neighbor in graph[node]:
            if not visited[neighbor]:
                que.append(neighbor)
                visited[neighbor] = True
                
    return result # 

# 입력 받는
# 노드(n), 간선(v) 
n, v, start_node = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(v):
    u, v_edge = map(int,input().split())
    graph[u].append(v_edge)
    graph[v_edge].append(u)
for i in range(1, n+1):
    graph[i].sort()
print(*(dfs(graph, start_node)))
print(*(bfs(graph, start_node)))


# 재귀 함수로 구현한 DFS 
# def dfs_recursive(graph, v, visited):
#     visited[v]  =True
#     print(v, end = ' ')
    
#     # 현제 노드와 연결된 다른 노드를 재귀적으로 방문 
#     for i in graph[v]:
#         if not visited[i]:
#             dfs_recursive(graph, i , visited)

# visited = [False]* (n+1)
# dfs_recursive(graph, start_node, visited)
