class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a,b = 0,0
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        a = i
                        b = j
                        return [a,b]