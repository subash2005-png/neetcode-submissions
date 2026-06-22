class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,num in enumerate(nums):
            com=target-num
            if com not in seen:
                seen[num]=i
            else:
                return [seen[com],i]
        return []
            
        