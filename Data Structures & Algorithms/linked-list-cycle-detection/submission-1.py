# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # slow and fast pointer approach
        slow, fast = head, head
        # move fast pointer two steps and slow pointer one step at a time
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
            # if they meet, there is a cycle
            if slow == fast:
                return True
        return False
        