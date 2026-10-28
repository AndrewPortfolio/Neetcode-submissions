class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s: string, k: number): number {
        let res = 0;
        const count = new Map<string, number>();

        let i = 0;
        let maxF = 0;
    
        for (let j = 0; j < s.length; j++) {
            const c = s[j];
            count.set(c, (count.get(c) || 0)+1) 

            maxF = Math.max(maxF, count.get(c))

            while ((j-i+1) - maxF > k) {
                let leftC = s[i]
                count.set(leftC, (count.get(leftC)!) - 1)
                i++
            }

            res = Math.max(res, j-i+1)

        }

        return res
    }
}
