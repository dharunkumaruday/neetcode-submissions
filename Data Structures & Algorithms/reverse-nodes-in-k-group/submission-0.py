class Solution:

  def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    group_prev = dummy

    while True:
      # Check if there are k nodes left
      curr = group_prev
      for _ in range(k):
        curr = curr.next
        if not curr:
          return dummy.next

      group_next = curr.next

      # Reverse k nodes
      prev, curr = group_next, group_prev.next
      for _ in range(k):
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

      # Connect with the previous group
      tail = group_prev.next
      group_prev.next = prev
      group_prev = tail