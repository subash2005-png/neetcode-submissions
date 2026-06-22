class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            s1={}
            t1={}
            for a,b in zip(s,t):
                if a not in s1:
                    s1[a]=1
                else:
                    s1[a]+=1

                if b not in t1:
                    t1[b]=1
                else:
                    t1[b]+=1
        
        return s1==t1


        