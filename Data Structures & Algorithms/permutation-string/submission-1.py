from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        w1 = len(s1)
        w2 = len(s2)

        if w2 < w1:
            return False
        
        w1_counter = Counter(s1)
        w2_counter = Counter(s2[:w1])

        if w1_counter == w2_counter:
            return True

        for i in range(w1, w2):
            w2_counter[s2[i]] += 1
            left = s2[i - w1]
            w2_counter[left] -= 1

            if w2_counter[left] == 0:
                del w2_counter[left]
            
            if w1_counter == w2_counter:
                return True
        return False
        
        

        