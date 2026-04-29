https://www.codetree.ai/ko/external-connection/classes/177/lectures/1798/curated-cards/challenge-collect-coins-easy/description
# from collection import deque
# comb
#1~9까지 3 개 고르기 그리고 3개가 모두 격자안에 있으면  S~E까지의 거리를 계산 
# 격자에 존재하지 않는 존재 dist = max.size
# if dist = sys.maxsize
# print(-1)
# C(R, M) = R C M 
# 재귀함수 o(2^N) >> 가지치기로 탐색 자체를 줄인다.

N = int(input())
grid = [list(input()) for _ in range(N)]

# arr = [i for i in range(1,10)]
# visited = [False]*(10)
num_lst = [] # grid 안에 있는 숫자 
combination = []
pos = {}

for i in range(N):
    for j in range(N):
        val = grid[i][j]
        if val == 'S':
            sr, sc =i, j
        elif val == 'E':
            er ,ec = i, j 
        elif val.isdigit():
            num_lst.append(int(val))
            pos[int(val)] = (i,j)
num_lst.sort() # 작은 수 ~ 큰수 순서대로 가야함 


def comb(depth,start,result):
    if depth == 3:
        combination.append(result[:])
        return
    for i in range(start,len(num_lst)):
        result.append(num_lst[i])
        comb(depth+1,i+1,result)
        result.pop()    
        
comb(0,0,[])

min_dist = float('inf')
for a in combination:
    dist = 0
    r1, c1 = pos[a[0]]
    r2, c2 = pos[a[1]]
    r3, c3 = pos[a[2]]
    dist += abs(r1-sr) + abs(c1 -sc)
    dist += abs(r2-r1) + abs(c2-c1)
    dist += abs(r3-r2) + abs(c3-c2)
    dist += abs(er-r3) + abs(ec -c3)
    
    if dist < min_dist:
        min_dist = dist
if min_dist == float('inf'):
    min_dist = -1
print(min_dist)

# def get_distance(p1,p2):
#     return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

# def make_per(arr,count,path):
    
#     if count==3:
#         result.append(path[:])

#     for i in range(len(arr)):
#         if not included[i]:
#             if not path or path[-1][0]<arr[i][0]:
#                 included[i] = 1
#                 path.append(arr[i])
#                 make_per(arr,count+1,path)
#                 path.pop()
#                 included[i] = False
                

# N = int(input())
# grid = [list(input()) for _ in range(N)]

# # Please write your code here.
# target_list = []
# result =[]

# for r in range(N):
#     for c in range(N):
#         if grid[r][c]!='.':
#             if grid[r][c] =='S':
#                 sr,sc = r,c
#             elif grid[r][c] =='E':
#                 gr,gc = r,c
#             else:
#                 target_list.append((int(grid[r][c]),r,c))
            
# #print(target_list)
# included = [0]*(len(target_list)+1)
# min_dist = float('inf')
# if len(target_list) < 3:
#     print(-1)

# else:
#     target_list.sort()
#     make_per(target_list,0,[])
#     for path in result:
#         dist = 0
#         curr = sr,sc
#         for target in path:
#             next = target[1],target[2]
#             dist += get_distance(curr,next)
#             curr = next
#         dist += get_distance(curr,(gr,gc))
#         min_dist = min(min_dist,dist)
#     print(min_dist)
