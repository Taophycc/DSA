// Difficulty - EASY
/*
function toLowerCase(s: string): string {
    return s.toLowerCase()
};
*/
// OR

/*
function toLowerCase(s: string): string {
    let result = ''
 
    for (let i = 0; i < s.length; i++) {
        if(s.charCodeAt(i) >= 65 && s.charCodeAt(i) <= 90){
            result += String.fromCharCode(s.charCodeAt(i) + 32);

        } else {
        result += s[i];
        }
    }
   return result
};
*/