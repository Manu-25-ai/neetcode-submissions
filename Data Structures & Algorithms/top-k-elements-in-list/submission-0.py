class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}
        for i in nums:
            if i in seen:
                seen[i]+=1
            else:
                seen[i]=1
        ans=sorted(seen, key=seen.get, reverse=True)        

        return ans[:k]    

        