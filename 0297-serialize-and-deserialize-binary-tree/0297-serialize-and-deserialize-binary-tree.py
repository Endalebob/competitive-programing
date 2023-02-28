# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        serilized = []
        deq = deque([[1,root]])
        self.max = 0
        def rec(node,h):
            self.max = max(self.max,h)
            if node:
                rec(node.left,h+1)
                rec(node.right,h+1)
        rec(root,0)
        while self.max:
            for i in range(len(deq)):
                idx,node = deq.popleft()
                if node:
                    serilized.append(str(idx)+'*'+str(node.val))
                    if node.left:
                        deq.append([idx*2,node.left])
                    if node.right:
                        deq.append([idx*2+1,node.right])
            self.max -= 1   
        serilized = ','.join(serilized)
        return serilized
                    
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        if not data:
            return
        data = data.split(',')
        dic = {}
        for i in data:
            a,b = i.split('*')
            dic[int(a)] = TreeNode(int(b))
        for i in dic:
            if i*2 in dic:
                dic[i].left = dic[i*2]
            if i*2+1 in dic:
                dic[i].right = dic[i*2+1]
        return dic[1]
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))