n=int(input()) # 수열의 크기 
lst_num =sorted(list(map(int,input().split()))) # 정렬이 필요하다 
x = int(input()) # 목표 숫자 


count = 0 # 갯수를 새기 위한 변수 
left, right = 0, n-1 # 투포인터 초기화 (0번 부터 ~ n-1 번까지 갯수)
while left < right:
    total = lst_num[left] + lst_num[right] # 두수의 합 
    if total == x: # 목표숫자와 이 두쌍이 일치한다면 
        count += 1 
        left += 1 # 왼쪽끝에서 줄이고
        right -= 1 # 오른쪽 끝에서 줄인다.
    elif total < x: # 목표숫자보다 작다면 
        left += 1 # 왼쪽의 수를 늘린다 
    else:
        right -= 1 # 목표숫자보다 크다면 오른쪽 수를 줄인다.
        
# 이 일련의 과정이 필요한 이유 total 이 두수의 합보다 작다면 수의 크기를 키워야 하기 때문에, 
# sort 된 리스트 내에서 현재의 left 포인터를 증가시키는 것이다.
# 반대로 total 이 두수의 합보다 크다면 수의 크기를 줄여야 하기 때문에 right 포인터를 감소시키는 것이다.

print(count)