class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic1={} #for count the frequency of a number
        rank=[] #sort rank according to frequency
        for i in nums:
            #count how many times a number occure in a dict
            if i not in dic1:
                # if the key is not created in dict then create it
                dic1[i]=0
                rank.append(i)
            # increases the number of count
            dic1[i]+=1
        #short the dict using sorted function 
        sort_value = dict(sorted(dic1.items(), key=lambda item: item[1]))
        rank = list(sort_value.keys())
        return rank[-k:]
