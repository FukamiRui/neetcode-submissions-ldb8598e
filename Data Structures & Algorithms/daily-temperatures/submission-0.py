class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        res = [0 for _ in range(len(temperatures))]

        for idx, val in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < val:
                prev = stack.pop()
                res[prev] = idx - prev
            stack.append(idx)
        return res        