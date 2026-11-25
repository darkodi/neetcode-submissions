# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1 -> 2 -> 3 -> None => 3 -> 2 -> 1 -> None
        prev, curr = None, head
        while curr:
            next_temp = curr.next  # point to the next node to save it before reversing the link
            curr.next = prev       # reverse the link
            prev = curr            # move prev to current node
            curr = next_temp       # move curr to the next node
        return prev  # when curr hits None, prev will be the new head of the reversed list
        