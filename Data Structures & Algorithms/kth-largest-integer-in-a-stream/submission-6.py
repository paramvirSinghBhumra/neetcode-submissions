class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        start = len(nums)-k if len(nums) > k else 0
        self.k_elements = sorted(nums)[start:]
        print(self.k_elements)

    def add(self, val: int) -> int:
        self.k_elements.append(val)
        self.k_elements = sorted(self.k_elements) if len(self.k_elements) <= self.k else sorted(self.k_elements)[1:]
        
        
        print("YEUH ",self.k_elements)

        return self.k_elements[0]
