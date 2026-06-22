class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen={}
        for elem in nums:
            if elem in seen:
                return True
            seen[elem]=1
        return False