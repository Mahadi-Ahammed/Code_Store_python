class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
#     input => [1,2,3,4]
#     prefix =>  [1,2,6,24]
#     postfix =>  [24,24,12,6]
    
#     ans = [1] [1,1,1,1] [1]
    
#     ans[i] => prefix[i - 1] * postfix[i + 1]
#     ans[0] => prefix[-1] * postfix[1]
#             => 1 * 24 
#             => [24 , 1 , 1 , 1]
#     ans[1]  => [24 , 12 , 8 , 6]
        ans = [1] * len(nums)                                   #[1,1,1,1]
        pre=nums[0]
                                        #store prefix multiplecations (i-1) in i start from 1
        for i in range(1,len(nums)):
            ans[i]=pre                  #[1,1,2,6]
            pre *=  nums[i]
                #go reverse to store postfix multiplecation and add in ans
        post=1
        for k in range(len(nums)-1,-1,-1):
            # print(k)
            ans[k]  *=   post
            post*= nums[k]
        return ans
