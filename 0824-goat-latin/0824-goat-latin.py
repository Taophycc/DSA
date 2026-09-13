class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowel = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        words = sentence.split()

        for i, word in enumerate(words):
            if word[0] in vowel:
                words[i] += "ma" + ("a" * (i + 1))
            else:
                words[i] = word[1:] + word[0] + "ma" + ("a" * (i + 1))

        return " ".join(words)
