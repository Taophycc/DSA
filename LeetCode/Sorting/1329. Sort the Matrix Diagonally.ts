// Difficulty - MEDIUM 
/*
function diagonalSort(mat: number[][]): number[][] {
     function helper(mat, i, j, len_row, len_col){
            let arr = []
            let a = i
            let b = j
            while (a < len_row && b < len_col){
                arr.push(mat[a][b])
                a++; b++;
            }
            arr.sort((a, b) => a - b)
            a = i; b = j;
            
            let c = 0
            while (a < len_row && b < len_col){
                mat[a][b] = arr[c]
                a++; b++; c++;
            }
        }
        let len_row = mat.length
        let len_col = mat[0].length
        for(let col = 0; col < len_col; col++){
            helper(mat, 0, col, len_row, len_col)
        }
        for(let row = 1; row < len_row; row++){
            helper(mat, row, 0, len_row, len_col)
        }
        return mat
};
*/