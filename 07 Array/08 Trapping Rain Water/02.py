### Calculating the amount of water using stack
### O(n)
def trap(height):
    stack = []
    volume = 0

    for i in range(len(height)):
        # when meeting saddle point
        while stack and height[i] > height[stack[-1]]:
            # pop from stack
            top = stack.pop()

            if not len(stack):
                break

            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]

            volume += distance * waters

        stack.append(i)
    return volume


input = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(input))