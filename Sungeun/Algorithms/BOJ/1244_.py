#1244
# 총 전구의 갯수
import sys

n = int(input())
# 초기 전구의 상태  # 1은 켜져있음 # 0은 꺼져있음 
# [-1] + list(map(int,input().split())) 를 사용하면 1~8번까지의 인덱스를 출력 가능 
lst_switch = [-1] + list(map(int, sys.stdin.readline().split()))
num_stu = int(input()) # 학생의 수 
# 남: 자신의 배수의 스위치를 조정 
# 여: 자신을 기준으로 대칭으로 구성된 곳까지 스위치를 조정
for _ in range(num_stu):
    sex, num = map(int, sys.stdin.readline().split()) #int # int
    # 여자 남자에 따라 동작이 다르므로 여남을 분류해줌
    if sex == 1: # 남자일때 
        for i in range(num,n+1, num): # 1~8 번 전구 중에 #num 의 배수를 가지고 있는 j 
            lst_switch[i] = 1 - lst_switch[i]
            # 스위치 전환 함수 
                 
    elif sex == 2:# 여자일때 
        lst_switch[num] = 1 - lst_switch[num]
        for d in range(1,n): # 1~n
            left_idx = num - d
            right_idx = num + d

            if left_idx >= 1 and right_idx <= n and lst_switch[left_idx] ==lst_switch[right_idx]:
                lst_switch[left_idx] = 1 - lst_switch[left_idx]
                lst_switch[right_idx] = 1 - lst_switch[right_idx]
                
            else:
                break

# print(*lst_switch)
for i in range(1,n+1):
    print(lst_switch[i], end = " ")
    if i%20 == 0:
        print()

# 인자확인을 잘하자!! 샤갈 