# prim 문제(정점기준으로 확장 )> 갈수 있는 노드들 중 가장 가중치가 적은 노드를 먼저 선택

import heapq

def prim(start,N,graph):
    visited = [False]*(N+1)
    visited[start] = True # 시작부분

    q = []
    ans = 0
    for edge in graph[start]: # 기준으로 갈수 있는 가장 가중치가 낮은 노드 
        heapq.heappush(q, edge)

    while q: 
        curr_cost, curr_node = heapq.heappop(q) # curr_cost, curr_node
        if visited[curr_node]: 
            continue
        ans += curr_cost
        visited[curr_node] = True
        for  next_cost, next_node in graph[curr_node]:
            if visited[next_node]:
                continue
            heapq.heappush(q, (next_cost, next_node))
    return ans
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    x_list = list(map(int,input().split()))
    y_list = list(map(int,input().split()))
    E = float(input())
    graph = [[] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if  i != j:
                dist = (x_list[i] -x_list[j])**2 + (y_list[i]-y_list[j])**2
                graph[i].append((dist,j))
    min_dist = prim(0,N,graph)
    min_val = round(E*min_dist)
    print(f'#{tc}',min_val)