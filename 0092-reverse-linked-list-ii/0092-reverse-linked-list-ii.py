# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: ListNode | None, left: int, right: int
    ) -> ListNode | None:
        dummy = ListNode(next=head)  # 假节点，防止left=1没法移动第一个节点的前一个
        p0 = dummy
        for _ in range(left - 1):  # 一直挪到left前一个节点
            p0 = p0.next

        pre = None
        cur = p0.next  # 此时为left节点所在location
        # 反转left-right之间所有节点，cur指向最后一位
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        p0.next.next = cur  # left后接上最后一位cur
        p0.next = pre  # left前的元素接上right
        return dummy.next

