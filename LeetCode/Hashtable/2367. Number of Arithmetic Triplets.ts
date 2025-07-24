// Difficulty -EASY
/*
function arithmeticTriplets(nums: number[], diff: number): number {
    const mySet = new Set(nums)
    let cnt = 0

    for(let i = 0; i< nums.length; i++){
        if(mySet.has((nums[i] + diff)) && mySet.has((nums[i] + (2*diff)))) {
            cnt++
        }
    }
    return cnt
};
*/