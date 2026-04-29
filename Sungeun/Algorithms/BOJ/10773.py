n = int(input())
stack = []

for t in range(n):
    n = int(input())
    if n != 0:
        stack.append(n)
    if n == 0:
        stack.pop()
print(sum(stack))

# #  스택 구현하기 
# class Stack:
#     def __init__(self):
#         self.stack = []
#     def push(self, data):
#         self.stack.append(data)
#     def pop(self):
#         if self.isEmpty():
#             return 'Stack is empty'
#         return self.stack.pop()
#     def isEmpty(self):
#         if self.isEmpty():
#             return len(self.stack)== 0
#     def peek(self):
#         if self.isEmpty():
#             return 'Stack is empty'
#         return self.stack[-1] #확인만 하는 명령어 
#     def top(self):
#         if self.isEmpty():
#             return 'Stack is empty'
#         return self.stack[-1] #len(stack)-1
    
# top 과 peek 의 차이
# top 은 스택의 가장 위쪽 요소를 가리키는 '위치'(포인터/index)  >> 현재 스택의 꼭대기가 어디인지 나타냄 >> 스택 데이터 구조의 상태(위치)
# peek 은 스택의 위쪽 요소를 조회하는 동작(method)  >> 제거하지 않고 값만 가져옴  >> 스택의 추상 자료형(ADT) 중 하나

#________________________________________________________
# 자바의 stack 클래스 >> vector 클래스 상속(extends) 받기에 Thread-Safe 하다는 특징이 있다 
# list 
# arraylist, linkedlist, Vector(stack)
# stack 클래스는 deprecated 되었다. 
# 어플리케이션에 스택 자료구조를 사용해야 할 상황일때, 자바의 스택 클래스는 쓰기를지양한다. vector 컬렉션을 상속받아 구현되었기 때문에
# 이 vectpr 컬렉션을 상속받아 구현되었기 때문, 이 vector 클래스 자체가 컬렉션 framework 가 나오지 전부터 오래된 클래스라 (취약점 많다)
# 상속으로 인한 부모 메서드 공유 문제 때문에 사용자가 잘못되게 사용될 수도 있따느 큰 문제점이 존재

# Stack 대신 Deque 사용 (양방향이 뚫린 stack)'
# push() -> insertion()
# pop() -> Deletion()