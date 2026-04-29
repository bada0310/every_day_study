left_stack = list(input().strip())
n = int(input())
right_stack = [] 
# 왼쪽으로 이동할때 abcd[입력] >> abc[입력]d 
# 이렇게 되면, abc 까지는 left_stack 에 넣고, 
# d 를 pop해서 오른쪽

# linked list = insert, pop() 의 시간 복잡도는 O(1)
# 어디에 넣고 빼고하는 그 어디(위치)를 찾는 것이 굉장히 어려운 리스트이다.O(n!) 

# deque(Deck)
# deque,linked list = 파이프 간들의 연결 사이에 특정 문자를 삽입/추출 하는 방식 
# C 계열에서는 '포인터'를 통해서 >> 끊어서 클래스의 사이즈를 찾는 방식 (초기에 클래스의 사이즈를 모름 )
# 파이썬으 클래스의 사이즈가 이미 정해져 있다 

# 스택을 활용하지 않고 리스트로 구현하려면 >> 슬라이싱을 활용 
# numbers = [10, 20, 30]
# 인덱스 1번 위치(10과 20 사이)에 15를 삽입
# numbers[1:1] = [15]
# print(numbers)             결과: [10, 15, 20, 30]

for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'L': # 왼쪽으로 한 칸
        if left_stack:
            right_stack.append(left_stack.pop())
    elif cmd[0] == 'D': # 오른쪽으로 한 칸 
        if right_stack:
            left_stack.append(right_stack.pop())
    elif cmd[0] == 'B': # 커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
        if left_stack:
            left_stack.pop()
    elif cmd[0] == 'P': # [P x] = x라는 문자를 커서 왼쪽에 추가함
        left_stack.append(cmd[1])
print("".join(left_stack+right_stack[::-1]))


# 참고 문헌 
# linked list 개념 이해: https://kururu.tistory.com/64
# Doubly linked list(python) 구현: https://cyr0331.tistory.com/27
