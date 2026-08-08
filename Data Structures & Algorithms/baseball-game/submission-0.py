class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for operation in operations:
            if operation == "+":
                a = stack[-1]
                b = stack[-2]

                stack.append(a + b)
            
            elif operation == "C":
                stack.pop()
            
            elif operation == "D":
                a = stack[-1]
                stack.append(a * 2)
            
            else:
                stack.append(int(operation))
            
        return sum(stack)
            

        