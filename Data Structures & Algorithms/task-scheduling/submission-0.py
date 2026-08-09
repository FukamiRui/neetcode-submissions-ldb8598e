from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        max_letter = max(count.values())
        max_count = list(count.values()).count(max_letter)

        sub_sum = (max_letter - 1) * (n + 1) + max_count
        
        return max(sub_sum, len(tasks))

        