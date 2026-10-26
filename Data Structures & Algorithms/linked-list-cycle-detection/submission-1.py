# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_set = set()

        while (head):
            old_size = len(visited_set)
            visited_set.add(head)
            
            if old_size == len(visited_set): #duplicate
                return True
            
            head = head.next
            

        return False