# row col 5*5 
finish = False 
board = []
speak  = []
count = 0 # 몇 번째 수를 부른 후 철
for _ in range(5): # 5줄을 입력 받는다 
    board.append(list(map(int,input().strip().split()))) # 보드에 들어가는 수 
    
for _ in range(5):
    speak.append(list(map(int,input().strip().split()))) # 사회자가 불러주는 수 
    
# 들어가는지 안들어가는지 를 확인하기 위한 보드를 하나더 만들 예정 
bingo = [[0]*5 for _ in range(5)]      #5* 5에 0 들이 채워진 보드 하나 만들기 

def check_row():
    res = 0 # 빙고 줄의 갯수 
    for i in range(5):
        cnt = 0
        for j in range(5):
            if bingo[i][j] == 1:
                cnt += 1
        if cnt == 5:
            res += 1
    return res

def check_col():
    res = 0
    for i in range(5):
        cnt = 0
        for j in range(5):
            if bingo[j][i] == 1:
                cnt += 1
        if cnt == 5:
            res += 1
    return res

def check_dia():
    res = 0 # 왼쪽 -> 오른쪽 아래 대각선 
    cnt1 = 0
    for i in range(5):
        if bingo[i][5-i-1] == 1:
            cnt1 += 1
    if cnt1 == 5:
            res += 1
    cnt2 = 0
    for i in range(5):
        if bingo[i][i] == 1:
            cnt2 += 1
    if cnt2 == 5:
        res += 1
    return res
        
cnt = 0

for i in range(5):
    for j in range(5): # 2차원 행렬에 조건을 부여하기 위한 기본 i, j 지칭 
        s = speak[i][j]
        count += 1 # 말하는거에 따라서 count += 씩 해주기 
        for y in range(5):
            for x in range(5):
                if board[y][x] == s:
                    bingo[y][x] = 1
        total = 0        
        total += check_row()
        total += check_col()  
        total += check_dia()
                
        if total >= 3:
            finish = True
            break
    if finish: break


print(count)
            





        
