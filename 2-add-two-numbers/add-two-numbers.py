
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = node = ListNode()
        while l1 or l2:
            if l1 and not l2: l2 = ListNode()
            elif l2 and not l1: l1 = ListNode()
            node_next_val, node.val = divmod(l1.val + l2.val + node.val, 10)
            node.next = ListNode(node_next_val) if node_next_val or l1.next or l2.next else None
            node, l1, l2 = node.next, l1.next, l2.next

        return ans
        