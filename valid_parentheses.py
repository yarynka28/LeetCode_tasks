class Solution:
    def isValid(self, s: str) -> bool:
        valid_dict = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for char in s:
            if char in valid_dict:
                stack.append(char)
            elif stack and valid_dict[stack[-1]] == char:
                stack.pop()
            else:
                return False
        return not stack
