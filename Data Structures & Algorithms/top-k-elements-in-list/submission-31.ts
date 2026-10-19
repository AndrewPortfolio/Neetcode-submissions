class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums: number[], k: number): number[] {
        const count = new Map<number, number>()
        // buckets to store each num freq that can occur in arr
        const freq = Array.from({length: nums.length+1}, () => [])

        // count up freq for each num
        for (const n of nums) {
            count.set(n, (count.get(n) || 0) + 1)
        }

        // store the freq counted for each num into corresponding bucket
        for (const [num, cnt] of count) {
            freq[cnt].push(num)
        }

        // return top k elements
        const res = []
        for (let i = freq.length-1; i > 0; i--) {
            for (const x of freq[i]) {
                res.push(x)
                if (res.length == k) {
                    return res
                }
            }
        }

    }
}
