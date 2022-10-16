class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = {}
        for i in strs:
            sortedstr = ''.join(sorted(i)) #sorted will return list so i need to join to conv them in str
            if sortedstr not in out:
                out[sortedstr]=[]
            # if sortedstr in out: #no need to check keys because all keys are added in upper line
            out[sortedstr].append(i)
        return out.values()
                