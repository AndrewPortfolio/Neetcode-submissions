class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s: string): boolean {
        const stack = [];
        const charSet = {
            ')': '(',
            ']': '[',
            '}': '{'
        };

        for (const c of s) {
            if (charSet[c]) {
                if (stack.length > 0 && stack[stack.length-1] === charSet[c]) {
                    stack.pop();
                }
                else {
                    return false;
                }
            }
            else {
                stack.push(c)
            }
        }
        return stack.length === 0;
    }
    

}
