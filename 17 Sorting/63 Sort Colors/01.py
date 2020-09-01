### Sort color using Dutch National Flag Problem
###
def sort_colors(nums):
    red, white, blue = 0, 0, len(nums)

    while white < blue:
        if nums[white] < 1:
            nums[red], nums[white] = nums[white], nums[red]
            white += 1
            red += 1
        elif nums[white] > 1:
            blue -= 1
            nums[white], nums[blue] = nums[blue], nums[white]
        else:
            white += 1


input = [2, 0, 2, 1, 1, 0, 2, 1, 0, 2, 1, 1, 0, 0, 2, 0, 0, 1, 1, 2, 1, 0]
sort_colors(input)
print(input)