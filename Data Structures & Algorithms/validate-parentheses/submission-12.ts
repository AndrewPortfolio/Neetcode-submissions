class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s: string): boolean {
        const stack = [];
        const par = {
            ')': '(',
            ']': '[',
            '}': '{',
        };

        for (const c of s) {
            if (par[c]) {
                if (stack.length > 0 && stack[stack.length-1] === par[c]) {
                    stack.pop();
                }
                else {
                    return false; 
                }
            }
            else {
                stack.push(c);
            }
        }
        
        return stack.length === 0;
    }
}
