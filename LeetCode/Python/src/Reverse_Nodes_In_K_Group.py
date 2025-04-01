class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        current = head
        while current and count < k:
            current = current.next
            count += 1
        if count == k:
            reversed_head = self.reverseKGroup(current, k)
            prev = None
            current = head
            for _ in range(k):
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            head.next = reversed_head
            head = prev                
        return head
