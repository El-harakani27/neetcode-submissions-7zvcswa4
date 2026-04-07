class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)> len(s2):
            return False

        dic_s1,dic_s2 = {ord('a')+i:0 for i in range(26)},{ord('a')+i:0 for i in range(26)}
        for i in range(len(s1)):
            dic_s1[ord(s1[i])] += 1
            dic_s2[ord(s2[i])] += 1
        if dic_s1 == dic_s2:
            return True
        l = 0
        for r in range(len(s1),len(s2)):
            dic_s2[ord(s2[r])] += 1
            dic_s2[ord(s2[l])] -= 1
            if dic_s1 == dic_s2:
                return True
            l+=1

            
        return False 