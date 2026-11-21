class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ssorted=sorted(s)
        tsorted=sorted(t)
        if len(ssorted)!=len(tsorted):
            return False
        for i in range(len(ssorted)):
            if ssorted[i]!=tsorted[i]:
                return False
        return True

        
