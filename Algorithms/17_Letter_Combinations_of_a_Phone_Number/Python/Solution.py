class Solution:
    def __init__(self):
        # digit to letter map for number pad
        self.numpad = {
            '0': '',
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        # list of letter combinations
        self.combinations = []

    def letterCombinationsHelper(self, letters: str, digits: str):
        # if there are no remaining digits, and if letters is not empty
        # then add to letter combinations
        if len(digits) < 1:
            if len(letters) > 0:
                self.combinations.append(letters)

            return

        # get current digit and its corresponding number pad letters
        current_digit = digits[0]
        numpad_letters = self.numpad[current_digit]

        # recursively generate combinations for every number pad letter
        for numpad_letter in numpad_letters:
            self.letterCombinationsHelper(
                letters + numpad_letter,
                digits[1:],
            )

    def letterCombinations(self, digits: str) -> List[str]:
        # call recursion with empty letters string
        self.letterCombinationsHelper('', digits)
        return self.combinations
