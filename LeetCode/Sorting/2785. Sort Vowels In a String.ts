// Difficulty - EASY
/*
function sortVowels(s: string): string {
  const vowelSet: Set<string> = new Set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']);  
    const chars: string[] = s.split('')
    const vowels: string[] = [] 
    const indices: number[] = []

    for(let i = 0; i< s.length; i++ ){
        if(vowelSet.has(s[i]) ){
            vowels.push(s[i])
            indices.push(i)
            
        }
    }
    vowels.sort()

    for(let i = 0; i<indices.length; i++){
        chars[indices[i]] = vowels[i]
    }
    return chars.join('')
};
*/
