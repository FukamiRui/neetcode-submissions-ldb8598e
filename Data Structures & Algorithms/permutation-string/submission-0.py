from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        w1 = len(s1)
        w2 = len(s2)

        if w2 < w1:
            return False
        
        w1_count = Counter(s1)
        w_count = Counter(s2[:w1])

        if w1_count == w_count:
            return True
        
        for i in range(w1, w2):
            w_count[s2[i]] += 1
            left = s2[i - w1]
            w_count[left] -= 1

            if w_count[left] == 0:
                del w_count[left]
            
            if w1_count == w_count:
                return True

        return False
        

        