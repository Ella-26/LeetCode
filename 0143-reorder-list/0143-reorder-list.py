# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def midNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 1. find mid and reverse后半段
        # 2. tmp1=head.next tmp2=head2.next  head.next=head2 head2.next=tmp1 head=tmp1 head2=tmp2
        mid = self.midNode(head)
        head2 = self.reverseList(mid)
        while head2.next:
            tmp = head.next
            tmp2 = head2.next
            head.next = head2
            head2.next = tmp
            head = tmp
            head2 = tmp2

