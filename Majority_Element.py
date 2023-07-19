class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numbers = {}
        result = 0
        maxNumber = 0

        for num in nums:
            numbers[num] = 1 + numbers.get(num,0)
            if numbers[num] > maxNumber:
                result = num
            maxNumber = max(maxNumber,numbers[num])
        return result