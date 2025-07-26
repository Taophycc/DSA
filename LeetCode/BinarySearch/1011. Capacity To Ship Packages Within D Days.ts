// Difficulty - MEDIUM
/*
function shipWithinDays(weights: number[], D: number): number {
  function canShip(capacity: number): boolean {
    let days = 1;
    let load = 0;
    for (const weight of weights) {
      if (load + weight > capacity) {
        days += 1;
        load = 0;
      }
      load += weight;
    }
    return days <= D;
  }

  let low = Math.max(...weights);
  let high = weights.reduce((acc, i) => acc + i, 0);

  while (low <= high) {
    const mid = Math.floor((low + high) / 2);
    if (canShip(mid)) {
      high = mid - 1;
    } else {
      low = mid + 1;
    }
  }
  
  return low;
}
*/