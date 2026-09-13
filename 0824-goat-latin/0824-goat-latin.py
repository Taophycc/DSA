class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()

        for i, word in enumerate(words):
            if word[0].lower() in "aeiou":
                words[i] += "ma"
            else:
                words[i] = word[1:] + word[0] + "ma" 
            
            words[i] += ("a" * (i + 1))

        return " ".join(words)
