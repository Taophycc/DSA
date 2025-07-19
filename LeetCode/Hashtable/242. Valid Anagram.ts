// Difficulty - EASY
/*
function isAnagram(s: string, t: string): boolean {
    if(s.length !== t.length) return false


    let arr1 = new Array(26).fill(0);
    let arr2 = new Array(26).fill(0);

    for (let i = 0; i < s.length; i++) {
        arr1[s.charCodeAt(i) - 'a'.charCodeAt(0)]++;
        arr2[t.charCodeAt(i) - 'a'.charCodeAt(0)]++;
    }

    for (let i = 0; i < 26; i++) {
        if (arr1[i] !== arr2[i]) return false;
    }

    return true;
};
*/