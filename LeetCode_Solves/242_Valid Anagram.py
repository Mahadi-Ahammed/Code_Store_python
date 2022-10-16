class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1={}
        if len(s)!=len(t):
            return False
        else:
            for j in s:
                if dic1.get(j)==None:
                    dic1[j]=1
                else:
                    dic1[j]+=1
            for i in t:
                if dic1.get(i)==None:
                    return False
                elif dic1[i]==0:
                    return False
                else:
                    dic1[i]-=1
            return True  
