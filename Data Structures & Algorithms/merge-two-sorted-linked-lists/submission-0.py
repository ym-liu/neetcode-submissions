# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        head = ListNode(None, None)
        curr = head

        while True:
            if head1 == None:
                curr.next = head2
                break
            if head2 == None:
                curr.next = head1
                break

            if head1.val < head2.val:
                temp = head1.next
                head1.next = None
                curr.next = head1
                curr = curr.next
                head1 = temp
            else:
                temp = head2.next
                head2.next = None
                curr.next = head2
                curr = curr.next
                head2 = temp

        return head.next
