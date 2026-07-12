class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        edited_words = []

        for query in queries:
            for dict_word in dictionary:
                diff_count = 0

                for i in range(len(query)):
                    if query[i] != dict_word[i]:
                        diff_count += 1
                    
                    if diff_count > 2:
                        break

                if diff_count <= 2:
                    edited_words.append(query)
                    break
        return edited_words