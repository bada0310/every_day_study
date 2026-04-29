
# 단방향 그래프에서 최단 경로를 구하는 문제입니다.
#MST 구하는 문제인가? 
# 자신의 집에서 - 인수의 집까지 왔다갔따 해야함 
# 다익스트라 문제 

import heapq
def dijkstra(start,N,graph):
    INF = float('inf')
    distance = [INF]*(N+1)
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        
        for next_node, cost in graph[now]:
            cost_sum = dist + cost

            if cost_sum < distance[next_node]:
                distance[next_node] = cost_sum
                heapq.heappush(q, (cost_sum, next_node))
    return distance

T = int(input())
for tc in range(1,T+1):
    N, M, X = map(int,input().split()) # node, edge, destination
    tree = [[] for _ in range(N+1)]
    rev_tree = [[] for _ in range(N+1)]

    for _ in range(M):
        s, e, cost = map(int,input().split())
        tree[s].append((e, cost))
        rev_tree[e].append((s,cost))
    way1 = dijkstra(X,N,tree)
    way2 = dijkstra(X,N,rev_tree)
    max_time = 0
    
    for i in range(1, N+1): # 모든 노드에 대해서
        ans = way1[i] + way2[i]
        if ans > max_time: max_time = ans
    print(f'#{tc}',max_time)