# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        dummy = ListNode(next=head)
        p0 = dummy
        pre = None
        cur = p0.next
        while n >= 2:  # 不足两个就不翻转
            n -= 2
            for _ in range(2):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            # 存下一个的头
            nxt = p0.next
            # 接上左右
            p0.next.next = cur
            p0.next = pre
            p0 = nxt
        return dummy.next

