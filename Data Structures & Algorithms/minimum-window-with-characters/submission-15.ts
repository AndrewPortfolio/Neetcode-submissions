class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {string}
     */
    minWindow(s: string, t: string): string {
        let countT = new Map<string, number>();
        let window = new Map<string, number>();

        for (const c of t) {
            countT.set(c, (countT.get(c) || 0) + 1);
        }

        const need = countT.size;
        let have = 0;

        let res = [-1, -1],
            resLen = Infinity;

        let i = 0;
        for (let j = 0; j < s.length; j++) {
            let c = s[j];
            window.set(c, (window.get(c) || 0) + 1);

            if (countT.has(c) && window.get(c) === countT.get(c)) {
                have++;
            }

            while (have === need) {
                if (resLen > j-i+1) {
                    resLen = j-i+1;
                    res = [i,j];
                }

                window.set(s[i], window.get(s[i])! - 1);
                if (countT.has(s[i]) && window.get(s[i]) < countT.get(s[i])) {
                    have--;
                }
                i++
            }
        }
        i = res[0];
        let j = res[1];

        if (resLen != Infinity) {
            return s.slice(i, j+1); 
        }
        return resLen === Infinity ? '' : s.slice(i, j+1)
    }
}
