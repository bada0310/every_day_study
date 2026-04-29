# 방문하지 않은 노드중 거리가 가장 짧은 노드의 번호를 찾는 법
def get_small_node(N,distance,visited):
    min_val = float('inf')
    idx = 0
    for i in range(1,N+1):
        if distance[i] < min_val and not visited[i]:
            min_val = distance[i]
            idx = i
    return idx 

def dijkstra(start,N,graph):
    INF = float('inf')
    distance = [INF]*(N+1)
    visited = [False]*(N+1)

    distance[start] = 0

    for _ in range(N+1):
        curr_N = get_small_node(N,distance,visited)
        visited[curr_N] = True
        for next_N, cost in graph[curr_N]:
            cost_sum = distance[curr_N] + cost
            if cost_sum < distance[next_N]:
                distance[next_N] = cost_sum
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