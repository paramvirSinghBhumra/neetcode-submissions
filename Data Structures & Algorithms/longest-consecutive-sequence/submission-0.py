class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums.sort()
        # print(nums)
        # first, second = 0,1
        # output = 0

        # for i in range(len(nums)):
        #     if nums[first] + 1 == nums[second]:
        #         second +=1
        #     else:
        #         output = second - first
        #         first += 1
        
        # return output

        sett = set(nums)
        output = 0

        for i in range(len(nums)):
            # find start number
            if nums[i]-1 not in sett:
                temp, cntr = nums[i],1
                while(temp+1 in sett):
                    cntr += 1
                    temp +=1
                output = cntr if cntr > output else output

        
        return output
            
        