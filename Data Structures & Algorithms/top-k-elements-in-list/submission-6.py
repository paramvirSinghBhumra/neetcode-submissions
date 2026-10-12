class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hash map 
        hash_map = {}

        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1
        
        # sort hash_map by values
        sorted_dict = {key: v for key, v in sorted(hash_map.items(), key=lambda item: item[1], reverse=True)}

        final_list = []
        for nums in sorted_dict:
            # print(f'{nums} -> {sorted_dict[nums]}')
            k-=1
            if k >= 0:
                final_list.append(nums)

            

        return final_list