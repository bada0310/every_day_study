# 시작은 북쪽 
# 결론은 도착 가능 = 1 도착 불가능 = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def move_command(r,c,command):
    global end_x, end_y
    curr_x, curr_y = r, c 
    curr_dir = 0
    for i in command:
        if i == 'A':
            nx, ny = curr_x + dx[curr_dir], curr_y + dy[curr_dir]
            if 0<= nx < N and 0<= ny < N and grid[nx][ny] != 'T':
                curr_x, curr_y =nx, ny
        elif i == 'L':
            curr_dir = (curr_dir+3)%4
        elif i == 'R':
            curr_dir = (curr_dir+1)%4
    if curr_x == end_x and curr_y == end_y:
        return 1
    return 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    grid = [input().strip() for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if grid[i][j] =='Y':
                end_x, end_y = i, j
            elif grid[i][j] =='X':
                start_x, start_y = i, j 
                
    Q = int(input()) # command cnt
    ans = [] # 정답 리스트 
    for _ in range(Q):
        n, command = input().split() # int, list
        res = move_command(start_x, start_y, command)
        ans.append(res)
    print(f'#{tc} {" ".join(map(str,ans))}')
