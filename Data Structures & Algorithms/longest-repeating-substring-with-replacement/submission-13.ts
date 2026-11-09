class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s: string, k: number): number {
        const window = new Map<string, number>();
        let maxLength = 0;

        let i = 0;
        for (let j = 0; j < s.length; j++) {
            window.set(s[j], (window.get(s[j]) | 0) + 1)

            let maxf = Math.max(...window.values());

            while (j-i+1-maxf > k) {
                window.set(s[i], window.get(s[i]) - 1);
                i++;
            }

            maxLength = Math.max(maxLength, j-i+1)
        }
        
        return maxLength;
    }
}
