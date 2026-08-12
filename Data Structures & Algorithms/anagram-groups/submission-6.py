class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #array of strings 
        #anagram = same length and same chars 
        #return anagrams grouped in any order

        #create a dict to store strings in group 
        res = defaultdict(list)

        #all strings in strs 
        for s in strs:
            count = [0] * 26 #empty array of lowercase alphabet a-z 
            #each char in string s
            for c in s:
                #inc count + 1 for each letter found 
                count[ord(c) - ord('a')] += 1
            #tuple makes count hashable and immutable --> no key error
            res[tuple(count)].append(s)

               #returns a list of values 
        return list(res.values())