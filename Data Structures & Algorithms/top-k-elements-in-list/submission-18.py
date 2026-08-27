class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #return the k most elements in nums 
        #1st count occurences of each num --> store into freq from 0-len(nums), min-max freq a number can be

        #{key:n  value:count}
        count = {}

        #initialize len(nums)+1(max freq) of empty buckets 
        freq = [[] for i in range(len(nums)+1)]

        #stores the counts of each number 
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        #stores the number into corresponding freq bucket by count
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        #return k most 
        for i in range(len(nums), 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
