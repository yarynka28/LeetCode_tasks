class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s = {}
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
        for char in t:
            count_s[char] = count_s.get(char, 0) - 1
            if count_s[char] < 0:
                return char
              
