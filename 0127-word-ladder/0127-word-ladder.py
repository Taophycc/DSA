class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dictionary_set = set(wordList)

        if endWord not in dictionary_set:
            return 0

        queue = deque([(beginWord, 1)])

        while queue:
            curr_word, curr_steps = queue.popleft()

            if curr_word == endWord:
                return curr_steps

            chars = list(curr_word)

            for i in range(len(curr_word)):
                original_char = chars[i]

                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == original_char:
                        continue

                    chars[i] = c
                    new_word = "".join(chars)

                    if new_word in dictionary_set:
                        queue.append((new_word, curr_steps+1))
                        dictionary_set.remove(new_word)

                chars[i] = original_char

        return 0