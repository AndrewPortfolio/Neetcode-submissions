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
            if (s[j] in seen) {
                i = Math.max(seen[s[j]] + 1, i);
            }
            seen[s[j]] = j;
            maxL = Math.max(maxL, j-i+1);
        }
        return maxL;
    }
}
