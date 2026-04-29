#1234
for t in range(1,11):
    N , arr = input().split()
    arr = list(arr)
    stack =[]
    for i in arr:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    answer =("".join(stack))
    print(f"#{t}",answer)