class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        prefix, postfix = [0 for i in range(len_nums)], [0 for i in range(len_nums)]

        running_product = 1
        for i in range(len_nums):
            running_product *= nums[i]
            postfix[i] = running_product

        running_product = 1
        for i in range(len_nums-1, -1, -1):
            running_product *= nums[i]
            prefix[i] = running_product

        
        arr = []
        # print("prefix=", prefix, "\npostfix=", postfix)
        for i in range(len_nums):
            prefix_value = 1 if i == 0 else postfix[i-1]
            postfix_value = 1 if i >= len_nums -1 else prefix[i+1]
            
            arr.append(prefix_value*postfix_value)

        return arr
        