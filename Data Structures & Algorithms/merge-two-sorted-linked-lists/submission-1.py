# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head: Optional[ListNode] = None
        ret_list: Optional[ListNode] = None

        while (list1 or list2):
            # get the smallest value node
            temp = None
            if (list1 and list2) and list1.val < list2.val:
                temp = list1
                list1 = list1.next
            elif list2:
                temp = list2
                list2 = list2.next
            elif list1:
                temp = list1
                list1 = list1.next

            # append temp node to list
            if not ret_list:
                ret_list = temp
                head = ret_list
            else:
                ret_list.next = temp
                ret_list = temp
            
            
        
        return head

                
        