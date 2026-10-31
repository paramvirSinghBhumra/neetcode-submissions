# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # reference head and keep going until you get tail.
        # remove reference to tail form second last element. (we need an edge case to catch lists that are less than 1?)
        # INSERT tail element after head and next.

        curr_head = head

        while(curr_head != None):
            next_node = curr_head.next

            curr = curr_head
            while(curr.next != None and curr.next.next != None):
                curr = curr.next
            if curr.next != next_node:
                curr_head.next = curr.next
                curr.next = None
                curr_head.next.next = next_node

            curr_head = next_node
        