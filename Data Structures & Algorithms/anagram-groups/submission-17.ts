class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs: string[]): string[][] {
        const res = new Map<string, string[]>()

        for (const s of strs) {
            const count = new Array(26).fill(0)
            
            for (let i = 0; i < s.length; i++) {
                const charCode = s[i].charCodeAt(0) - 'a'.charCodeAt(0)
                count[charCode]++
            }
            const key = count.join('#')
            if (!res.has(key)){
                res.set(key, [])
            }
            res.get(key)!.push(s)
        }

        
        return Array.from(res.values())
    }
}
