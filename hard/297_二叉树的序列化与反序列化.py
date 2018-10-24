# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if not root:
            return "#";
        return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right);
        
        

    def deserialize(self, data):
        root = self.getTree(data.split(","));
        return root;
        
    def getTree(self,data):
        if len(data) <= 0:
            return None;
        node = None;
        val = data.pop(0);
        if val != "#":
            node = TreeNode(val);
            node.left = self.getTree(data);
            node.right = self.getTree(data);
        return node;
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))