# 스택의 push/pop/size/top/empty 연산을 구현하는 문제
import sys
stack = []
def push(line):
    if 'push' in line:
        stack.append(line[1])

def top():
    if not stack:
        print(-1)
    else:
        print(stack[-1])

def size():
    if 'size' in line:
        print(len(stack))

def empty():
    if not stack:
        print(1)
    else:
        print(0)
        
def pop():
    if not stack:
        print(-1)
    else:
        print(stack.pop())
        
        
n = int(input())      
for _ in range(n):
    input = sys.stdin.readline
    line = input().split()
    if line[0] =='push':
        push(line)
    if line[0] == 'top':
        top()
    if line[0] =='size':
        size()
    if line[0] =='empty':
        empty()
    if line[0] =='pop':
        pop()