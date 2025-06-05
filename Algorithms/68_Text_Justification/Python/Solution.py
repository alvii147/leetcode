class Solution:
    def evenlyDivideNumbers(self, n, m):
        '''
        Create list of n numbers that are as evenly divided as possible and add up to m.
        '''
        nums = [0] * n
        for i in range(n):
            num = (m // n)
            # if numbers aren't evenly divided, add one to each number
            if m % n != 0:
                num += 1

            nums[i] = num
            m -= num
            n -= 1

        return nums

    def maxWordFit(self, words: List[str], maxWidth: int) -> int:
        '''
        Counts maximum number of words that would fit in a line.
        '''
        wordCount = 0
        lineLength = 0
        for word in words:
            wordLen = len(word)
            if lineLength + wordLen > maxWidth:
                break

            wordCount += 1
            lineLength += wordLen + 1

        return wordCount

    def formLine(self, words: List[str], width: int) -> str:
        '''
        Given list of words, form a line by filling in spaces between words to reach given width.
        '''
        numOfWords = len(words)
        wordLenSum = sum([len(w) for w in words])
        numOfSpaces = width - wordLenSum

        # handle corner case of single word
        if numOfWords == 1:
            return words[0] + (' ' * numOfSpaces)

        spaceLens = self.evenlyDivideNumbers(numOfWords - 1, numOfSpaces)

        line = ''
        for i in range(numOfWords):
            line += words[i]
            if i < numOfWords - 1:
                line += ' ' * spaceLens[i]

        return line

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        while len(words) > 0:
            numWordsInLine = self.maxWordFit(words, maxWidth)
            # handle corner case of last line
            if numWordsInLine == len(words):
                line = ' '.join(words)
                lines.append(line + (' ' * (maxWidth - len(line))))
                break

            line = self.formLine(words[:numWordsInLine], maxWidth)
            lines.append(line)
            words = words[numWordsInLine:]

        return lines
