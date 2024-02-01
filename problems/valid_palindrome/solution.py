class Solution:
    def isPalindrome(self, s: str) -> bool:
        phrase = "".join(letter for letter in s if letter.isalnum()).lower()
        return phrase == phrase[::-1]