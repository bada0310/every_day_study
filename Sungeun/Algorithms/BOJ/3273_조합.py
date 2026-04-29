# O(n)
n=int(input())
# 기존의 순서를 지켜야 한다는 요건이 없음
lst_num =sorted(list(map(int,input().split()))) # 정렬로 봐야할 조합의 가짓수를 줄임 
x = int(input())
#조합으로 모든 가짓수의 쌍을 만듦 > ex.(1,2) 합을 구함 > 합이 x 와 일치하는지 확인

count = 0
left, right = 0, n-1
while left < right:
    total = lst_num[left] + lst_num[right]
    if total == x:
        count += 1
        left += 1 # 인덱스 늘리기 
        right -= 1
    elif total < x:
        left += 1
    else:
        right -= 1

print(count)

# 추가 설명(모든 조합을 탐색할 필요가 없는 이유)  
# sorted 되어있는 리스트기에, 'left'를 옮겼다는건, left' 와 right 사이의 어떤 수를 가져와도 지금의 right 를 더했을 때 x 보다 작다는 뜻
# 반대로 right 를 옮겺다는건, 어떤 수를 가져와도 지금의 left 와 더했을때 x 보다 크다는 뜻  
# 쉽게 얘기하자면 어차피 2개의 숫자를 뽑아야 하는데 목표 x에 대해 1과 X-1 에서 부터 X/2 X/2 가 될때까지 조금씩 차이를 줄여나가며 숫자를 찾는 방법


# O(n^2)         
# n=int(input())
# lst_num =sorted(list(map(int,input().split())))
# x = int(input())

# count = 0
# for i in range(n):
#     for j in range(i+1,n)
#         # total = lst_num[i] + lst_num[j]
#         if lst_num[i] + lst_num[j] == x:
#             count += 1
# print(count) 
