# answer = binary
# relation map needed (양방향 dict)
# 연결고리를 확인하는 문제 >> 재귀
# 하나로 길게 이어져있는지 확인
import sys
input() = sys.stdin.readline()
N, M = map(int,input().split())
relation = {i:[] for i in range(N)}
for _ in range(M):
    key, val = map(int,input().split())
    if key not in relation: relation[key] = []
    if val not in relation: relation[val] = []
    relation[key].append(val)
    relation[val].append(key) # 양방향 dict
    
visited = [False]*N

def dfs(now, depth):
    if depth == 4: # A-B-C-D-E 관계가 4개 
        
        return True
    visited[now] = True # 시작점 true
    
    for next in relation[now]:
        if not visited[next]:
            if dfs(next, depth+1):
                return True
    visited[now] = False # 백트래킹 
    return False

ans = 0

for i in range(N):
    if dfs(i, 0):
        ans = 1
        break
print(ans)

# 노드 번호에 관계없이실제 관계망에 참여한 노디끼리만 연결되어있는가를 확인해야한다!! 