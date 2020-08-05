### Get temperature list and output how many days to wait till facing hotter day using stack.
### Values stored in stack are ordered.
def daily_temperatures(T):
    answer = [0] * len(T)
    stack = []
    for i, cur in enumerate(T):
        while stack and cur > T[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)

    return answer


T = [73, 74, 75, 71, 69, 72, 76, 73]
print(daily_temperatures(T))