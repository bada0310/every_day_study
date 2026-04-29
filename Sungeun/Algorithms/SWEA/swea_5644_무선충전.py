# BC 범위 내에 충전량을 입력 + 충전량이 최대 충전량보다 크면 최대 충전량으로 입력
# D = |XA – XB| + |YA – YB| 마름도 모양의 범위를 구하는 func 정의
# 이동 경로따라 충전량 받기 (시계열로 이동하면서 충전량 받기)

# 단지 번호 붙이기 
def put_charge_map(x,y,C,P,bc_idx):
    cen_x, cen_y = x-1, y-1
    for i in range(10):
        for j in range(10):
            if abs(i- cen_y) + abs(j-cen_x) <= C:
                grid[i][j].append((bc_idx, P))

def move(x, y,dir):
    dx = [0, 0, 1, 0, -1]
    dy = [0, -1, 0, 1, 0]
    return x + dx[dir], y + dy[dir]

def charge_bc(ax, ay, bx, by):
    global total_charge
    for i in range( M+1):
        if i > 0:
            ax, ay = move(ax, ay, move_a[i-1])
            bx, by = move(bx, by,move_b[i-1])

        a_charge = grid[ay][ax]
        b_charge = grid[by][bx]
        
        # 둘다 범위 밖
        if not a_charge: a_charge = [(-1, 0)]
        if not b_charge: b_charge = [(-2, 0)]
        
        max_sum = 0
        
        for a_id, a_p in a_charge:
            for b_id, b_p in b_charge:
                if a_id == b_id and a_id != -1:
                    sum_val = a_p
                else:
                    sum_val = a_p + b_p
                if sum_val > max_sum:
                    max_sum = sum_val
        total_charge += max_sum

T = int(input())
for tc in range(1,T+1):
    grid = [[[] for _ in range(10)] for _ in range(10)]
    M, A = map(int,input().split())
    move_a = list(map(int,input().split()))
    move_b = list(map(int,input().split()))
    for idx in range(A):
        x, y, C, P = map(int,input().split())
        put_charge_map(x,y,C,P,idx)
    total_charge = 0
    charge_bc(0,0,9,9)
    print(f'#{tc}',total_charge)

# test 2
# 포인트를 A, B 의 이동에 두지 말고 
# 딱 그 T = t 인 순간에 두개를 비교한다고 생각하면 다른 방법도 있을 수 있을 듯하다 
