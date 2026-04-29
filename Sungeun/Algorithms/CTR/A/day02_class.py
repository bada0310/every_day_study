# 1이 3개 이상 있는 위치
# 숫자 0과 1로만 이루어진 N×N 크기의 격자 상태가 주어집니다. 
# 각 칸 중 상하좌우로 인접한 칸 중 숫자 1이 적혀 있는 칸의 수가 3개 이상인 곳의 개수를 세는 프로그램을 작성해보세요. 
# 단, 인접한 곳이 격자를 벗어나는 경우에는 숫자 1이 적혀있지 않은 것으로 생각합니다.

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
node_count = 0
for r in range(n):
    for c in range(n):
        s = 0
        for i in range(4):
            
            nr = r + dx[i]
            nc = c + dy[i]

            if 0 <= nr < n and 0<= nc < n:
                s += grid[nr][nc]
        if s >= 3:
            node_count += 1
print(node_count)         

# n = int(input())
# grid = [list(map(int, input().split())) for _ in range(n)]

# # Please write your code here.
# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]

# count = 0
# for r in range(n):
#     for c in range(n):
#         total = 0


#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
            
#             if 0<= nr <n and 0<= nc <n:
#                 total += grid[nr][nc]
#         if total >= 3:
#             count += 1
#         else:
#             pass
        
# print(count)

# 2. 작은 구슬의 이동
# 벽으로 둘러싸인 N 행 N 열의 격자 안에 한 개의 구슬이 놓여져 있습니다. 
# 이 구슬은 상하좌우 중 특정 방향으로 1초에 한 칸씩 움직입니다.

# 가장 왼쪽 위 격자 칸을 1행 1열, 가장 오른쪽 아래 격자 칸을 N 행 N 열이라고 합시다. 
# 아래의 그림은 초기에 1행 2열에 놓여 있고 왼쪽을 향하는 구슬을 나타낸 것입니다.
# 구슬이 벽에 부딪히면 움직이는 방향이 반대로 뒤집혀 동일한 속도로 움직이는 것을 반복합니다. 
# 이때 방향을 바꾸는 데에는 1만큼의 시간이 소요됩니다.

n, t = map(int, input().split()) # 4 4
r, c, d = input().split() # 1 2 L
r, c = int(r) - 1, int(c) -1

# Please write your code here.
mapper = {'R': 0, 'D': 1, 'U': 2, 'L': 3}
dr, dc= [0, 1, -1, 0], [1, 0, 0, -1]

dir_num = mapper[d]
def in_range(r, c): # 범위 내에 존재하는지 확인 
    return 0<= r and r < n and 0<= c and c < n

for _ in range(t):
    nr, nc = r + dr[dir_num], c + dc[dir_num]

    if in_range(nr, nc):
        r, c = nr, nc
    else:
        dir_num = 3 - dir_num
print(r+1, c+1)