# 17471_게리멘더링
# 두 인구의 차이만 구하면된다.
combinations= [] # rlfhremf fltmxm 
res = []
def comb(depth,start,limit):
    if depth == limit:
        combinations.append(res[:]) # shallow copy
        return
    for i in range(start,N+1):
        res.append(i)
        comb(depth+1,i+1,limit)
        res.pop()

from collections import deque
def bfs(group): #bfs# groupA 와 groupB 각각 따로 해서 
    start  = group[0]
    q = deque([start])
    visited = set([start]) #
    
    while q:
        cur_node = q.popleft()
        
        for n in graph[cur_node]:
            if n in group and n not in visited:
                visited.add(n)
                q.append(n)
    if len(visited) == len(group):
        return True
    else:
        return False    
        

def count_human(group): # arr 에 있는 인구 수 세는 함수 
    total = 0
    for i in group:
        total += peoples[i-1]
    return total

N = int(input()) #node 갯수
peoples = list(map(int,input().split()))
graph = [[] for _ in range(N+1)]

for v in range(1,N+1):
    lst = list(map(int,input().split())) # 2 2, 4 
    for k in range(1, lst[0]+1):
        graph[v].append(lst[k])
for i in range(1,N//2+1):
    comb(0,1,i) # 1~N 까지
    
min_ans = float('inf')
for groupA in combinations:
    groupB = []
    for i in range(1,N+1):
        if i not in groupA:
            groupB.append(i) # 나머지를 groupB 에 넣음
    # check is a group
    if bfs(groupA) and bfs(groupB):
        total_A = count_human(groupA)
        total_B = count_human(groupB)
        diff = abs(total_A - total_B)
        if diff < min_ans:
            min_ans = diff
if min_ans == float('inf'):
    print(-1)
else:
    print(min_ans)