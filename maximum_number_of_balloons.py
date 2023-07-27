class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dict_of_letters = {"b":0, "a":0, "l":0, "o":0, "n":0}
        for char in text:
            if char in dict_of_letters.keys():
                dict_of_letters[char] += 1
        max_words = min(dict_of_letters["b"], dict_of_letters["a"], dict_of_letters["l"] // 2, dict_of_letters["o"] // 2, dict_of_letters["n"])
        return max_words
