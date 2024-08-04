class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
          return False
        sortedS = "".join(sorted(s))
        sortedT = "".join(sorted(t))
        
        for i in range(len(sortedS)):
            if sortedS[i] != sortedT[i]:
                return False
            
        return True