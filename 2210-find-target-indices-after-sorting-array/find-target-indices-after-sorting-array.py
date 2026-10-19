class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        
        r=sorted(nums,reverse=False)
        ans=[]

        for i in range(0,len(r)):
            if r[i] == target:
                ans.append(i)
            else:
                continue

        return ans
