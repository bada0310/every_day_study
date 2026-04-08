# 최소 비용 문제, 음수가 존재하지 않음===> dijkstra 문제 
# 시작점 끝점 고정 
# 
dx = [0,1,0,-1]
dy = [1,0,-1,0]
import heapq
def is_range(r,c):
    return 0<= r <N and 0<= c < N 

def dijkstra(N,graph): # 2dimention
    INF = float('inf')
    dist = [[INF]*N for _ in range(N)]
    q = []
    heapq.heappush(q,(0,0,0)) # 좌표 및 cost 
    dist[0][0] = 0

    while q:
        cd, cx, cy  =heapq.heappop(q) # curr_val, curr_x, curr_y

        if cd > dist[cx][cy]:
            continue
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if is_range(nx,ny):
                nd = cd + graph[nx][ny]
                if nd < dist[nx][ny]:
                    dist[nx][ny] = nd
                    heapq.heappush(q,(nd, nx, ny))
    return dist
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    grid = [list(map(int, input().strip())) for _ in range(N)]
    ans = dijkstra(N,grid)
    print(f'#{tc}',ans[N-1][N-1])