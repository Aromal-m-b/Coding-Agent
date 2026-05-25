class Solution:
    def check(self, nums: list[int]) -> bool:
        if len(nums) < 2:
            return True
        else:
            temp = nums[0]
            for i in range(1,len(nums)):
                if temp>nums[i]:
                    if nums[i:len(nums)] + nums[0:i]  == sorted(nums):
                        print(nums[i:len(nums)] + nums[0:i])
                        return True
                    break
                if i == len(nums)-1:
                    return True
                temp = nums[i]
        return False

obj = Solution()
print(obj.check([1,4,1,2,3,5]))