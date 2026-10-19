class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs: string[]): string {
        let encoded = ""
        for (const s of strs) {
            encoded += String(s.length)
            encoded += '#'
            encoded += s
        }

        return encoded
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str: string): string[] {
        const res = []
        let decoded = ""
        let i = 0
        while (i < str.length) {
            let j = i
            while (str[j] != '#') {
                j += 1
            }
            const length = Number(str.slice(i,j))
            i = j + 1
            decoded = str.slice(i, j+length+1)
            res.push(decoded)
            i = j + 1 + length
        }

        return res
    }
}
