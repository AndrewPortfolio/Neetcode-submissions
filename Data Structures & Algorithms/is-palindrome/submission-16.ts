class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s: string): boolean {
        let i = 0 
        let j = s.length - 1
        const isalnum = (str: string): boolean => /^[a-zA-Z0-9]+$/.test(str)

        while (i < j) {
            while (i < j && !isalnum(s[i])) {
                i++
            }
            while (i<j && !isalnum(s[j])) {
                j--
            }

            if (s[i].toLowerCase() !== s[j].toLowerCase()) {
                return false
            }

            i++
            j--
        }

        return true

    }
}
