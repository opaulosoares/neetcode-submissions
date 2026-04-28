class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        auxDict = {}

        for i, item in enumerate(nums):
            if auxDict.get(item, 0) >= 1:
                return True
            else:
                auxDict[item] = 1
        
        return False