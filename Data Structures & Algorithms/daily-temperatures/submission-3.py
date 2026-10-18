class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr = [0 for i in range(len(temperatures))] # create output array filled with 0s, with the same size as temperatures
        stack = [] # touple stack (value, index)

        # items have to be in DECREASING ORDER
        for i in range(len(temperatures)):
            # [0,1,2,5,3,1,0,5,4]
            # [1,1,1,0,3,2,1,0,0]
        
            while len(stack) > 0 and stack[-1][0] < temperatures[i]:
                val, index = stack.pop()
                arr[index] = i - index

            stack.append((temperatures[i], i))

        return arr