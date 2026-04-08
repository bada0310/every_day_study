# 사이클을 제거하고 (union-find) 모든 노드를 포함하는 트리 
# 1<=T<=50, 1<=V<=1000, 1<=w<=10, 1<=E<=1000000
# kruskal algorithms (MST) (greedy)

# def find(parent,x): # find parent
#     if parent[x] != x:
#         parent[x] = find(parent, parent[x])
#     return parent[x]

def find(parent,x):
    root = x
    while parent[root] != root:
        root = parent[root]
    curr = x
    while curr != root:
        next_node = parent[curr]
        parent[curr] = root
        curr = next_node
    return root 

def union(parent, a, b): #grouping (make cycle)
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def kruskal(V,edges): # use union and find
    parent = [i for i in range(V+1)] # parent node list 

    total_cost = 0 
    for cost, start, end in edges:
        if find(parent,start) != find(parent, end):
            union(parent,start,end)
            total_cost += cost
    return total_cost

T = int(input())
for tc in range(1, T+1):
    N ,E = map(int,input().split())
    edges = []
    for _ in range(E):
        start, end, cost = map(int,input().split())
        edges.append((cost, start, end))
    
    edges.sort() # important
    res = kruskal(N,edges)
    print(f'#{tc}',res)

# try2 (prim)

import heapq   
def prim(start,N,tree):
    visited = [False]*(N+1)
    visited[start] = True
    Q = []
    ans = 0
    for edge in tree[start]:
        heapq.heappush(Q,edge)

    while Q:
        curr_cost, node = heapq.heappop(Q)
        if visited[node]:
            continue
        ans += curr_cost
        visited[node] =True
        for next_cost, next_node in tree[node]:
            if visited[next_node]:
                continue
            heapq.heappush(Q,(next_cost, next_node))
    return ans

T = int(input())
for tc in range(1, T+1):
    N ,E = map(int,input().split())
    tree = [[] for _ in range(N+1)]
    
    for _ in range(E):
        s, e, cost = map(int,input().split())
        tree[s].append((cost, e))
        tree[e].append((cost, s))
    res = prim(0,N,tree)
    print(f'#{tc}',res)

# 