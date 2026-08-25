class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s_nums = set(nums)
        max_seq = 0

        for num in nums:
            seq = []
            ln = num - 1
            if ln in s_nums:
                continue
            
            seq.append(num)
            
            rn = num + 1
            if rn in s_nums:
                seq.append(rn)
                while rn != None:
                    rn += 1
                    if rn in s_nums:
                        seq.append(rn)
                    else:
                        rn = None 


            
            max_seq = max(max_seq, len(seq))
        
        return max_seq
        
