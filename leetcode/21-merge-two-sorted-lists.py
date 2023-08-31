class ListNode:
  def __init__(self, val = 0, next = None):
    self.val = val
    self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        """
        Merges two sorted linked lists into a single sorted linked list.

        Args:
        list1 (ListNode): The head node of the first sorted linked list.
        list2 (ListNode): The head node of the second sorted linked list.

        Returns:
        ListNode: The head node of the merged sorted linked list.
        """
        head = tail = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # attach remaining nodes, if any
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return head.next

list01 = ListNode(1)
list01.next = ListNode(2) 
list01.next.next = ListNode(4)

list02 = ListNode(1)
list02.next = ListNode(3)
list02.next.next = ListNode(4)
list02.next.next.next = ListNode(5)
list02.next.next.next.next = ListNode(6)

solution = Solution()
merged_list = solution.mergeTwoLists(list01, list02)

current = merged_list
while current:
    print(current.val, end=" -> ")
    current = current.next  