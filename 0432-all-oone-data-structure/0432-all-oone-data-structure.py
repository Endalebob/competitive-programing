class ListNode:
    def __init__(self, frequency):
        self.val = frequency
        self.data = set()
        self.pre = None
        self.next = None


class AllOne(object):

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next, self.tail.pre = self.tail, self.head
        self.memo = {}
        
    def add(self, node, key):
        if node.val + 1 != node.next.val:
            newNode = ListNode(node.val + 1)
            newNode.pre, newNode.next = node, node.next
            newNode.pre.next = newNode.next.pre = newNode
        else:
            newNode = node.next
        
        newNode.data.add(key)
        return newNode
    
    def add_prev(self, node, key):
        if node.val - 1 != node.pre.val:
            newNode = ListNode(node.val - 1)
            newNode.pre, newNode.next = node.pre, node
            newNode.pre.next = newNode.next.pre = newNode
        else:
            newNode = node.pre
        newNode.data.add(key)
        return newNode
        
    def inc(self, key):
        if key not in self.memo:
            self.memo[key] = self.add(self.head, key)
        else:
            node = self.memo[key]
            self.memo[key] = self.add(node, key)
            node.data.remove(key)
            if not node.data:
                node.pre.next, node.next.pre = node.next, node.pre
                node.next = node.pre = None

    def dec(self, key):
        if key in self.memo:
            node = self.memo[key]
            node.data.remove(key)
            del self.memo[key]
            if node.val > 1:
                self.memo[key] = self.add_prev(node, key)
            if not node.data:
                node.pre.next, node.next.pre = node.next, node.pre
                node.next = node.pre = None
                

    def getMaxKey(self):
        if not self.tail.pre.data:
            return ""
        num = self.tail.pre.data.pop()
        self.tail.pre.data.add(num)
        return num

    def getMinKey(self):
        if not self.head.next.data:
            return ""
        num = self.head.next.data.pop()
        self.head.next.data.add(num)
        return num
