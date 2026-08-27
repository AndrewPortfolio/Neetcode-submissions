class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #iterate through strs --> count the char count for each string --> return anagrams together 

        res = {}

        #counts each char count in each string 
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            #{key: count, value: s} --> count is mutable --> tuple makes it imuttable --> keys have to be immutable
            # res[tuple(count)].append(s)
            res.setdefault(tuple(count), []).append(s)

        return list(res.values())