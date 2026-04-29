# 최소 이동 거리 -> bfs 탐색 
# start end cost 
import heapq

def dijkstra(start,N,graph): # O(ElogV)
    INF = float('inf') # infinity
    distance = [INF]*(N+1) # 각 노드 까지의 최종 거리

    q = []
    heapq.heappush(q,(0,start))
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
    N, E = map(int, input().split())
    tree = [[] for _ in range(N+1)]
    for _ in range(E):
        start, end, cost = map(int,input().split())
        tree[start].append((end,cost))

    res = dijkstra(0,N,tree)
    print(f'#{tc}', res[N])
            
