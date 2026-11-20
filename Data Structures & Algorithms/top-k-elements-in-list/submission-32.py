class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # {key: number, val: occurences}
        count = {}
        
        # count occurences of each number
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # store counts into corresponding buckets
        freq = [[] for _ in range(len(nums) + 1)]
        for num, cnt in count.items(): 
            freq[cnt].append(num)
        
        res = []
        #return most freq nums 
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res
        
