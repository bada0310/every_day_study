# swea 12399
T =int(input())
for t in range(1, T+1):
    text = input()
    stack = []

    for i in text:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)


    print(f"#{t} {len(stack)}") 