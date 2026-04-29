# 요구사항
# 연속된 세 개의 계단을 모두 밟아서는 안 된다
# 맨마지막 계단을 밟아야 한다 
# why? 
# 이전 칸에서 했던 정보를 기억해서 이후에 활용하겠다 
# 총 점수의 최댓값을 출력 
# 이전까지의 연산의 결과값을 넣어준 것 = dp table? 

# idx +1 은 하면 안되는 행위 -> 내가 갈수 있는 모든 경우에 대해서 오류를 범하기 떄문에
# 규칙을 지킨다는 보장을 할 수 없게 된다. 
# idx + 2 , idx +2 +1 (이렇게 되면 )
N = int(input())
stairs = []
dp = [0]*N #  답은 dp[N-1]  

for _ in range(N):
    stairs.append(int(input()))

dp[0] = stairs[0] # ? 초기값 설정
if N > 1: # 길이가 1 딱뎀인경우 
    dp[1] = stairs[0] + stairs[1]
if N > 2: # 길이가 2딱뎀인 경우 
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2]) 

for idx in range(3,N):
    dp[idx] = max(dp[idx-2] + stairs[idx], dp[idx-3] + stairs[idx-1] + stairs[idx])
    
print(dp[N-1])

for idx in range(N):
    if idx+2 < N :
        dp[idx+2] = max(dp[idx]+stairs[idx+2], dp[idx+2])
    if idx+3 < N:
        dp[idx+3] = max(dp[idx]+stairs[idx+2]+stairs[idx+3], dp[idx+3])
print(dp[N-1])