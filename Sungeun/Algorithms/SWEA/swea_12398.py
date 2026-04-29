# swea 12398 
import sys
sys.stdin = open("sample_input.txt", "r")
# def dfs(start_node):
#     stack = [start_node]
#     visited = []
#     while stack:
#         node =stack.pop()
#         if node not in visited:
#             visited.append(node)
#             # 자식 노드들을 스택에 담음
#             stack.extend(graph[node])
#     return visited
def dfs(V):
    visited


def dfs(graph, S, G):
    stack = [S]
    visited = set()
    visited.add(S)
    while stack:
        curr_node = stack.pop()
        if curr_node == G:
            return 1
        for neighbor in graph.get(curr_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
    return 0

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split()) # node = V= edge
    graph = {}
    for info in range(E):
        n, v = map(int,input().split())
        if n not in graph:
            graph[n] = [] # key-val 자리를 만들어준다
        graph[n].append(v) # 단 방향

    S, G = map(int, input().split())
    answer = dfs(graph, S, G)
    print(f"#{t}",answer)
