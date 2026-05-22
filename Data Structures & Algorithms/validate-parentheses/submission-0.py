class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closed_dict = {"]": "[", "}": "{", ")": "("}


        if not s:
            return True
        
        for char in s:
            if char in closed_dict:
                if stack and stack[-1] == closed_dict[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
        