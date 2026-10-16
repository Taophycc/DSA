class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        letters = []
        digits = []

        for log in logs:
            identifier, content = log.split(" ", 1)

            if content[0].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        
        letters.sort(key=lambda x: (x.split(" ", 1)[1], x.split(" ", 1)[0]))

        return letters + digits