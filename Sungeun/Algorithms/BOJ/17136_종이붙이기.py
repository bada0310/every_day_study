grid = [list(map(int,input().split())) for _ in range(10)]
paper_lst = [5]*5 
min_ans = float('inf')
# 이미 [1 * size for _ in range(size)] 가 맞다는 전제로 
def can_attach(r,c,size): # N * N 인지 확인하는 것 
    if r +size > 10 or c + size > 10:
        return False # r,c 부터 시작해서 범위 밖에 넘어가도= 실패 
    for x in range(r,r+size):
        for y in range(c,c+size):
            if grid[x][y] == 0:
                return False # 0 이 존재해도 실패 
    return True # 존재 
# _________________________________________________

def color_grid(r,c,size,state):
    for x in range(r, r+size):
        for y in range(c, c+size):
            grid[x][y] = state 
# 백트래킹을 위한 switching 함수 
# ________________________________________
# def check_paper(r,c):
#     global min_ans
    

def dfs():
    global min_ans
    curr_page = 25 - sum(paper_lst)
    if curr_page >= min_ans:
        return
    for r in range(10): 
        for c in range(10):
            if grid[r][c] == 1:
                for size in range(5,0,-1):
                    if can_attach(r,c,size) and paper_lst[size-1] > 0: # 종이가 남아있다면
                        color_grid(r,c,size,0)
                        paper_lst[size-1] -= 1  # 존재하면 값을 더해준다.  # idx = size -1
                        
                        dfs()

                        color_grid(r,c,size,1)   #backtracking 
                        paper_lst[size-1] += 1
                return
    min_ans = min(min_ans, curr_page)


# 실행부
dfs()
# 5개 이상 썼는지 확인하기 
if min_ans == float('inf'):
    print(-1)
else:
    print(min_ans)

# grid = [list(map(int,input().split())) for _ in range(10)]
# paper_lst = [5]*5 
# min_ans = float('inf')
# # 이미 [1 * size for _ in range(size)] 가 맞다는 전제로 
# def can_attach(r,c,size): # N * N 인지 확인하는 것 
#     if r +size > 10 or c + size > 10:
#         return False # r,c 부터 시작해서 범위 밖에 넘어가도= 실패 
#     for x in range(r,r+size):
#         for y in range(c,c+size):
#             if grid[x][y] == 0:
#                 return False # 0 이 존재해도 실패 
#     return True # 존재 
# # _________________________________________________

# def color_grid(r,c,size,state):
#     for x in range(r, r+size):
#         for y in range(c, c+size):
#             grid[x][y] = state 
# # 백트래킹을 위한 switching 함수 
# # ________________________________________
# def check_paper(r,c):
#     global min_ans
#     for size in range(5,0,-1):
#         if can_attach(r,c,size) and paper_lst[size-1] > 0: # 종이가 남아있다면
#             color_grid(r,c,size,0)
#             paper_lst[size-1] -= 1  # 존재하면 값을 더해준다.  # idx = size -1
#             min_ans = sum(paper_lst)
#             dfs()
#     #backtracking 
#             color_grid(r,c,size,1)
#             paper_lst[size-1] += 1

# def dfs():
#     for r in range(10): #(0~9 )
#         for c in range(10):
#             if grid[r][c] == 1:
#                 check_paper(r,c)
#             else:
#                 return

# # 실행부
# # 5개 이상 썼는지 확인하기 
# for i in paper_lst:
#     if i < 0: # 각각의 요소는 5를 넘을 수 없다 
#         ans = -1
#     else:
#         ans = min_ans
# print(ans)