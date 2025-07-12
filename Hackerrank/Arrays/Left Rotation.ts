/*
function rotateLeft(d: number, arr: number[]): number[] {
    // Write your code here
 const actualRotate = d % arr.length;
  const init = [];
  let i = 0;

  for (; i < actualRotate; i++) {
    init.push(arr[i]);
  }

  let cnt = 0;
  let p = i;
  for (; p < arr.length; p++) {
    arr[cnt] = arr[p];
    cnt++;
  }

  let end = arr.length - init.length;
  for (let j = 0; j < init.length; j++) {
    arr[end] = init[j];
    end++;
  }
  return arr;
}
rotateLeft(2, [1,2,3,4,5]); 
*/