# 14888
N = int(input())
arr = list(map(int,input().split()))
arr_func = list(map(int,input().split())) # only 4
max_val = -float('inf')
min_val = float('inf') # tip! 

def dfs(depth, curr_total):
    global max_val, min_val
    
    if depth == N: # 끝에 도달했을때의 결과 
        max_val = max(curr_total, max_val)
        min_val = min(curr_total, min_val)
        return
    
    next_num = arr[depth]
    
    if arr_func[0] > 0:
        arr_func[0] -= 1
        dfs(depth+1, curr_total + next_num)
        arr_func[0] += 1 # 백트래킹 
        
    if arr_func[1] > 0:
        arr_func[1] -= 1
        dfs(depth+1, curr_total - next_num)
        arr_func[1] += 1 # 백트래킹 
        
    if arr_func[2] > 0:
        arr_func[2] -= 1
        dfs(depth+1, curr_total * next_num)
        arr_func[2] += 1 # 백트래킹 
        
    if arr_func[3] > 0:
        arr_func[3] -= 1
        dfs(depth+1, int(curr_total / next_num))
        arr_func[3] += 1 # 백트래킹 
dfs(1,arr[0])

print(max_val)
print(min_val)

# 사칙 연산 리스트 만들기 
# ops = ['+','-','*','//']
# for i in range(4):
#     for _ in range(arr_func[i]):
#         four_basic.append(ops[i])
# 를 할 필요가 없다. 사이 순서대로 넣을 때마다 arr_func 에서 지워나가면 되기 때문에 
# if not visited  대신 arr_fucn 에서 얼마나 사용됐는지를 체크하는 방식으로 만들기 

# 숫자는 그대로 (고려할 필요 X) 
# 연산자만 나열( 같은 것이 있는 연산자들의 나열, 중복 순열과는 약간 다른 개념) 
# 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다.