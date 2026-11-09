class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s: string): boolean {
        const brackets = {
            ')':'(',
            ']':'[',
            '}':'{'
        };
        const stack = [];

        for (const c of s) {
            if (c in brackets) {
                if (stack.length > 0 && stack.at(-1) === brackets[c]) {
                    stack.pop();
                } else {
                    return false;
                }
            } else {
                stack.push(c);
            }
        }

        return stack.length === 0;
        

    }
}
