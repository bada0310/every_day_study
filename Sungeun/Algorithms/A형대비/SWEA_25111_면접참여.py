# swea_25111_면접참여 
# 민호는 정확히 M개의 문제를 맞혔습니다. 하지만 문제가 나온 순서는 기억하지 못합니다.
# 민호가 받을 수 있는 최소 점수를 출력하세요.
# 11011 이런식으로 1은 맞춘것 0은 틀린것 

# greedy
MOD = 1000000009
 
T = int(input())
for tc in range(1, T + 1):
    n, m, k = map(int, input().split())
    safe = (n - m) * (k - 1) # safe = 틀린문제 들을 맞은 문제 사이에 배치 

 
    if m <= safe: 
# 만약 내가 맞힌 개수($m$)가 safe보다 작거나 같다면, 
# 틀린 문제들을 잘 배치해서 한 번도 연속 k번에 도달하지 않게 만들 수 있습니다. 
# 따라서 별도의 계산 없이 그냥 m이 최종 점수가 됩니다.

        print(f'#{tc} {m % MOD}')

    else:

        extra = m - safe #초과분이 생기는 상황 
        full = extra // k
        rem = extra % k
        score = (pow(2, full + 1, MOD) - 2) * k % MOD
        print(f'#{tc} {(score + rem + safe) % MOD}')