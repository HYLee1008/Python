### Find the index of the target using binary search by binary search module
###
def search(nums, target):
    try:
        return nums.index(target)
    except:
        return -1