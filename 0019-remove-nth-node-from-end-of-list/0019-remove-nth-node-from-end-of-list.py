# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(next=head)
        left = dummy
        right = dummy

        for _ in range(n):  # right走n步等left
            right = right.next

        while right.next:  # right走到最后时此时left是n前面一个节点
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next

