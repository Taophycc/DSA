// Difficulty - EASY
/*
// Using the inbuilt sorting method
function transformArray(nums: number[]): number[] {
     
     for(const [idx, val] of nums.entries()){
        if(val % 2 == 0){
            nums[idx] = 0
        } else {
            nums[idx] = 1
        }
     }
     nums.sort()
    return nums
}
*/

/*
// Using bubbleSort algortihm
function transformArray(nums: number[]): number[] {
  for (let i = 0; i < nums.length; i++) {
    nums[i] = nums[i] % 2 === 0 ? 0 : 1;
  }

  for (let i = 0; i < nums.length; i++) {
    let swapped = false;
    for (let j = 0; j < nums.length - i - 1; j++) {
      if (nums[j] > nums[j + 1]) {
        let temp = nums[j];
        nums[j] = nums[j + 1];
        nums[j + 1] = temp;
        swapped = true;
      }
    }
    if (!swapped) break;
  }
  return nums;
};
*/