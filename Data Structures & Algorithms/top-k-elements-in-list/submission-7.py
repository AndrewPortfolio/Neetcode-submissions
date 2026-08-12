class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #hashmap to store count {key:# value:count}
        count = defaultdict(int)

        #count occurences of each num in nums
        for n in nums:
            count[n] += 1

        #create len(nums) # of buckets, index in freq represents count of occurences
        freq = [[] for _ in range(len(nums) + 1)]
        #store each num into it's corresponding freq = index
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        #return k top freq elements, start at the end bc that is the most occurences poss
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
