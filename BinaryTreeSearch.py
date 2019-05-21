class BinTreeNode(object):
 
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
 
       
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree

def delete_item(tree, item):  # Week 6, Task 1

    if tree is None:  # looking for the node to be deleted
        return tree
    elif item > tree.value:  # going through the tree..
        tree.right = delete_item(tree.right, item)
    elif item < tree.value:
        tree.left = delete_item(tree.left, item)
    # when you find the node, there are 3 cases
    else:
        if tree.left == None and tree.right == None:  # Case 1: Easiest. No child. Just delete the node.
            tree = None
            return tree
        elif tree.left is None:  # Case 2: There is only one child. A little bit more complex.
            val = tree.right #establish link between parent node and child node
            tree = None
            return val
        elif tree.right is None:
            val = tree.left
            tree = None
            return val
        else:  # Case 3: Node has 2 children. The hardest.   #find successor, delete it, replace the node to be deleted with the successor
            temp = minimum_itemval(tree.right)
            tree.value = temp.value
            tree.right = delete_node(tree.right, temp.value)
    return tree
 
def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print (tree.value)
 
def in_order(tree):
    if(tree.left!=None):
        in_order(tree.left)
    print (tree.value)
    if(tree.right!=None):
        in_order(tree.right)
 
if __name__ == '__main__':
   
  t=tree_insert(None,6);
  tree_insert(t,10)
  tree_insert(t,5)
  tree_insert(t,2)
  tree_insert(t,3)
  tree_insert(t,4)
  tree_insert(t,11)
  delete_item(t, 3)
  in_order(t)
  

