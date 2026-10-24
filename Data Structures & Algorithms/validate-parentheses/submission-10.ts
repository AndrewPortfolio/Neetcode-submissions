class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s: string): boolean{ 
        const valid = new Map<string,string> ([
            [')','('], 
            [']','['], 
            ['}','{']
        ])

        const stack = []

        for (const c of s) {
            if (valid.has(c)) {
                if (stack && stack.at(-1) === valid.get(c)) {
                    stack.pop()
                }
                else {
                    return false
                }
            } else {
                stack.push(c)
            }
        }

        return stack.length === 0
    }
}
