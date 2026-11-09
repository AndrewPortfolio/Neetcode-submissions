class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s: string): number {
        let seen = new Map<string, number>();
        let maxL = 0;

        let i = 0;
        for (let j = 0; j < s.length; j++){
            if (seen.has(s[j])) {
                i = Math.max(seen.get(s[j]) + 1, i);
            }
            seen.set(s[j], j); 
            maxL = Math.max(maxL, j-i+1);
        }
        return maxL;
    }
}
