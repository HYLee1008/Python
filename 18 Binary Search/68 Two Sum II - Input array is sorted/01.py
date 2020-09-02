### Find the index of the array that can make the target number by summation using two pointer
### O(n)
def two_sum(numbers, target):
    left, right = 0, len(numbers) - 1
    while not left == right:
        if numbers[left] + numbers[right] < target:
            left += 1
        elif numbers[left] + numbers[right] > target:
            right -= 1
        else:
            return left + 1, right + 1