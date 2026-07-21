class Solution:
    def isValid(self, s: str) -> bool:
        closures = {")": "(", "]": "[", "}": "{"}
        stack = []

        for i in s:
            if i in closures:
                if stack and stack[-1] == closures[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return not stack
                
            

        