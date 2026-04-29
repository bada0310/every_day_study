#12915
# 트리 생성: 중위 순회
# 트리 탐색: 전위 순회 
# point 
# 중위 순회 하게 되면 노드(기준) 으로,
# left 작은idx 의 원소들만 들어갈수 있고 
# right 큰 idx 원소들만 들어갈수 있다. 
# 
def build_tree(N):
    tree = [0]*(N+1) # 0 idx(+1)
    curr_num = 1
    def in_order(node_idx):
        nonlocal curr_num
        if node_idx > N: # over_head 막아주기 
            return
        in_order(node_idx*2)

        tree[node_idx] = curr_num
        curr_num += 1 # val 키워주기 

        in_order(node_idx*2+1)
    in_order(1)

T = int(input()) 
for t in range(1, T+1):
    N = int(input())
    result = build_tree(N)
    print(f'#{t}',result[1], result[N//2])