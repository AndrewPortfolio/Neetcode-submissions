class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s: string): number {
        const seen = new Set<string>();
        let maxLength = 0;

        let i = 0;
        for (let j = 0; j < s.length; j++){
            while (seen.has(s[j])) {
                seen.delete(s[i]);
                i++;
            }
            let length = j-i+1;
            seen.add(s[j]);
            maxLength = Math.max(length, maxLength)
        }
        return maxLength;
    }
}
