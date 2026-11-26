# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy node to serve as the head of the merged list
        dummy = ListNode()
        current = dummy 

        # traverse both lists and append the smaller value to the merged list
        while list1 and list2:
            if list1.val < list2.val:
                #link the current node to list1 and move list1 forward
                current.next = list1
                list1 = list1.next
            else:
                #link the current node to list2 and move list2 forward
                current.next = list2
                list2 = list2.next
            # move the current pointer forward in the merged list
            current = current.next
        # append any remaining nodes from list1 or list2 to the merged list
        current.next = list1 or list2
        return dummy.next
        