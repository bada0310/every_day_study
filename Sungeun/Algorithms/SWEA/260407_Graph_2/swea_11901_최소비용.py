# 최소 비용 
# start /end 고정
# 기본적인 이동시에 1만큼의 연료
# 높이가 다르면 높이 차이만큼의 연료가 추가로 든다. (nx,ny 가 x,y)
import heapq

def dijkstra(N, graph):
    INF = float('inf')
    dist_graph = [[INF]*N for _ in range(N)]

    q = []
    start_cost = 0
    heapq.heappush(q, (start_cost, 0, 0))
    dist_graph[0][0] = start_cost

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q: 
        dist, x, y  = heapq.heappop(q)

        if dist_graph[x][y] < dist:
            continue
        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]
            if 0<= nx < N and 0<= ny < N:
                height_diff = max(0, grid[nx][ny] - grid[x][y]) 
                cost_sum = dist + 1 + height_diff

                if cost_sum < dist_graph[nx][ny]:
                    dist_graph[nx][ny] = cost_sum
                    heapq.heappush(q, (cost_sum, nx,ny))
    return dist_graph[N-1][N-1]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    grid = [list(map(int,input().split())) for _ in range(N)]
    res = dijkstra(N, grid)
    print(f'#{tc}',res)
