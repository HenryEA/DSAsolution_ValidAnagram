class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        tracker = Node(0)
        curr, stack = tracker, [head]

        while stack: 
            temp = stack.pop()
            if temp.next:
                stack.append(temp.next)
            if temp.child:
                stack.append(temp.child)
            curr.next = temp
            temp.prev = curr
            temp.child = None
            curr = temp
        tracker.next.prev = None
        return tracker.next
            

