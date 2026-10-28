class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s: string): number {
        let i = 0;
        let maxLength = 0;
        const map = new Map<string, number>()

        for (let j = 0; j < s.length; j++) {
            if (map.has(s[j])) {
                i = Math.max(map.get(s[j])!+1,i)
            }
            map.set(s[j],j)
            maxLength = Math.max(maxLength, j-i+1)
        }
        
        return maxLength
    }
}
