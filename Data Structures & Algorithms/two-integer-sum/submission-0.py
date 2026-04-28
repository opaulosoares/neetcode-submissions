class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevDict = {}

        for index, item in enumerate(nums):
            diff = target - item
            if diff in prevDict:
                return [prevDict[diff], index]

            prevDict[item] = index
        
        return
            