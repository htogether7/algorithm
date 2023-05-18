class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        products = [1] * len(nums)
        reverse_products = [1] * len(nums)

        for index in range(len(nums)):
            if index == 0:
                products[index] *= nums[index]
            else:
                products[index] = products[index-1] * nums[index]

        for index in range(len(nums)-1,-1,-1):
            if index == len(nums)-1:
                reverse_products[index] *= nums[index]
            else:
                reverse_products[index] = reverse_products[index+1] * nums[index]
        
        for index in range(len(nums)):
            tmp = 1
            if index == 0:
                tmp *= reverse_products[index+1]
            elif index == len(nums)-1:
                tmp *= products[index-1]
            else:
                tmp *= reverse_products[index+1]
                tmp *= products[index-1]
            answer.append(tmp)
        
        return answer
