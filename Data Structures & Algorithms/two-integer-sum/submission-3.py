class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
            v= target-nums[i]
            # for j in range(i+1,len(nums)):
            #     if v==nums[j]:
            #         return [i,j]
            if v in seen:
                return[seen[v],i]
            seen[nums[i]]=i







        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target and i!=j:
        #             return [i,j] 
                  
