### Find the largest number that can be obtained by combining given number using insert sort
###
class Solution:
    @staticmethod
    def to_swap(n1, n2):
        return str(n1) + str(n2) < str(n2) + str(n1)

    def largestNumber(self, nums):
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j - 1], nums[j]):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1
            i += 1

        return str(int(''.join(map(str, nums))))


sol = Solution()

print(sol.largestNumber([10, 2]))
print(sol.largestNumber([3, 30, 34, 5, 9]))