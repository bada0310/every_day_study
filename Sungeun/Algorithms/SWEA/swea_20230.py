#swea_20230
T =int(input())
for t in range(1, T+1):
    N, M = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(N)]
 
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0] # delta 
     
    max_val = 0
    for r in range(N):
        for c in range(M):
 
            s = board[r][c] 
 
            for i in range(4):
                for k in range(1, N):
                    nr = r + dr[i]* N
                    nc = c + dc[i]* N
                    if 0 <= nr < N and 0 <= nc < M:
                        s += board[nr][nc]
 
            if max_val < s:
                max_val = s
    print(f"#{t} {max_val}")

# T =int(input())
# for t in range(1, T+1):
#     N = int(input())
#     board = [list(map(int,input().split())) for _ in range(N)]
 
#     dr = [0, 1, 0, -1]
#     dc = [1, 0, -1, 0]
     
#     max_val = 0
#     for r in range(N):
#         for c in range(N):
 
#             s = board[r][c]
 
#             for i in range(4):
#                 for k in range(1, N):
#                     nr = r + dr[i]* k
#                     nc = c + dc[i]* k
#                     if 0 <= nr < N and 0 <= nc < N:
#                         s += board[nr][nc]
 
#             if max_val < s:
#                 max_val = s
#     print(f"#{t} {max_val}")