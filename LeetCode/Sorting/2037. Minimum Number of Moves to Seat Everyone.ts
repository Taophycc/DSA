// Difficulty - EASY
/*
function minMovesToSeat(seats: number[], students: number[]): number {
    seats.sort((a, b) => a - b);
    students.sort((a, b) => a - b);
    let sum = 0

    for(let i = 0; i< students.length; i++){
        sum += Math.abs(seats[i] - students[i]);
    }
    return sum
};
*/