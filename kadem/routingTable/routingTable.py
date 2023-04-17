from dataStructures import treeNode

class RoutingTable:
    #id - 160 bit sha1 id
    #k - global paramter which represents bucket size
    def __init__(self, id : int, k : int) -> None:
        self.id = id
        self.k = k
        self.root = treeNode.TreeNode(True, k, self.id)
    
    def insertNewNode(self, id : int) -> None:
        if id == self.id:
            print("Why am I adding myself")
            return
        currentNode = self.root
        parent = None
        #need to keep track of parent as that where the break happens, exceptional case for when root gets split
        currentInsertIdBit = id
        currentIdBit = self.id
        while not (currentIdBit>>160)^(currentInsertIdBit>>160):
            moveBit = currentInsertIdBit>>160
            if (moveBit and not currentNode.right) or (not moveBit and not currentNode.left) :
                if parent:
                    newLeaf = treeNode.TreeNode(True, self.k, -1)
                    newSubRoot  = treeNode.TreeNode(False, self.k, -1)
                    if moveBit:
                        newSubRoot.right = currentNode
                        newSubRoot.left = newLeaf
                    else:
                        newSubRoot.left = currentNode
                        newSubRoot.right = newLeaf
                    shiftedRight = parent.right is currentNode
                    if shiftedRight:
                        parent.right = newSubRoot
                    else:
                        parent.left = newSubRoot
                    currentNode = newSubRoot
                else:
                    newRoot = treeNode.TreeNode(False, self.k, 0)
                    newLeaf = treeNode.TreeNode(True, self.k, -1) #idk how to do the prefix thing rn
                    self.root = newRoot
                    if moveBit:
                        newRoot.right = currentNode
                        newRoot.left = newLeaf
                    else:
                        newRoot.left = currentNode
                        newRoot.right = newLeaf
            parent = currentNode
            currentInsertIdBit << 1
            currentIdBit << 1
            if moveBit:
                currentNode = currentNode.right
            else:
                currentNode = currentNode.left
        moveBit = currentInsertIdBit>>160
        if parent:
            if moveBit:
                if parent.right:
                    parent.right.bucket.append(id)
                else:
                    parent.right = treeNode.TreeNode(True, self.k, id)
            else:
                if parent.left:
                    parent.left.bucket.append(id)
                else:
                    parent.left = treeNode.TreeNode(True, self.k, id)
        else:
            newRoot = treeNode.TreeNode(False, self.k, 0)
            newLeaf = treeNode.TreeNode(True, self.k, id)
            self.root = newRoot
            if moveBit:
                newRoot.left = currentNode
                newRoot.right = newLeaf
            else:
                newRoot.right = currentNode
                newRoot.left = newLeaf

        #while msb the same
            #if the appropraite direction is availavble (1 -> right, 0 left)
                #move in that direction and shift the bits as needed
            #else
                #this means you are at the lowest kbucket which has not been expanded yet
                #you need to go to the parent change it to be a new intermediary
                #split into 2 buckets
                #move into the appropraite one
        #u are at the first node which is in contention
        #go up to parent
            #if not parent 
                #  you are at the root on first split and it differs at first bit
                # make a new root node and split it, and go there and add ur self
            #else
                #go up to parent and see if k bucklet exists, if yes add yourself if no make it and add yourself

    def getKClosestNodes():
        pass