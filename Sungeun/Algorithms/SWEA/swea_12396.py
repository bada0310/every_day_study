# swea 12396 
# 정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력한다.
T =int(input())
for t in range(1, T+1):
    text = input()
    top = -1
    stack = [0] * len(text)
    ans = 1
    for i in text:
        if i in '{(':
            top += 1
            stack[top] = i
        
        elif i in ')}':
            if top == -1:
                ans = 0
                break
            curr_top = stack[top]
            if (i == ')' and curr_top =='(') or (i == '}' and curr_top == '{'):
                top -= 1
            else:
                ans = 0
                break
    if top != -1:
        ans = 0
    print(f"#{t} {ans}")