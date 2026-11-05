/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortByReflection = function(nums) {
    function reverseBinary(n) {
        let reversed = 0;
        while (n > 0) {
            reversed = (reversed << 1) | (n & 1);
            n >>= 1;
        }
        return reversed;
    }

    nums.sort((a, b) => {
        const reversedA = reverseBinary(a);
        const reversedB = reverseBinary(b);

        if(reversedA !== reversedB) return reversedA - reversedB;
        return a - b;
    });

    return nums;
};