/*
function hourglassSum(arr: number[][]): number {
    // Write your code here
    let maxsum = -Infinity;
   for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr[i].length; j++) {
    if(i ===0 || i=== arr.length -1|| j=== 0|| j=== arr[i].length-1){
       continue 
    }
    let sum = arr[i][j] + arr[i-1][j]+arr[i-1][j-1]+arr[i-1][j+1] +arr[i+1][j] + arr[i+1][j-1]+ arr[i+1][j+1];
    if (sum > maxsum){
        maxsum = sum;
    }
  }
}
return maxsum;
}
*/
