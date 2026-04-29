#1231
# 트리는 완전 이진 트리 형식으로 주어지며, 
# 노드당 하나의 문자만 저장할 수 있다.
#  tree 배치 : 전위 순회 (pre-order) rot -left -right-left-right
#  tree 탐색 : 중위 순회 (in-order) left - root - right

import sys
input = sys.stdin.readline

def in_order(idx):
    if idx > N:
        return
    in_order(idx*2)
    print(tree_val[idx], end= ' ')
    in_order(idx*2+1)

for t in range(1, 11):
    N = int(input())
    tree_val = [0] * (N+1)
    for _ in range(N):
        data = input().split() # idx, val, child_nodes
        node_idx = data[0]
        node_val = data[1]
        child = list(map(int,data[2:]))
        tree_val[node_idx] = node_val
    print(f'#{t}',end = ' ')
    in_order(1)
    print()