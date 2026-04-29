# MST problem 
# 첫째 줄에 정점의 개수 V(1 ≤ V ≤ 10,000)와 간선의 개수 E(1 ≤ E ≤ 100,000)
# prim 
import heapq
def prim(start,N,tree):
    visited = [False]*(V+1)
    visited[start] = True
    Q = []
    ans = 0
    for edge in tree[start]:
        heapq.heappush(Q,edge)

    while Q:
        curr_cost, node =heapq.heappop(Q)
        if visited[node]:
            continue
        ans += curr_cost
        visited[node] = True
        for next_cost, next_node in tree[node]:
            if visited[next_node]:
                continue
            heapq.heappush(Q,(next_cost,next_node))
    return ans


V, E = map(int,input().split())
tree = [[] for _ in range(V+1)]
for _ in range(E):
    s, e, val = map(int,input().split())
    tree[s].append((val, e))
    tree[e].append((val, s))
res = prim(s,V,tree)
print(res)