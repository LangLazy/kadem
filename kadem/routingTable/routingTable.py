from dataStructures import treeNode
from collections import deque 

def getBinary(num, digs):
    ans = ""
    mask = 1
    for i in range(digs):
        if num&mask == 0:
            ans += "0"
        else:
            ans += "1"
        num>>1
    return ans[::-1]

class RoutingTable:
    #id - 160 bit sha1 id
    #k - global paramter which represents bucket size
    def __init__(self, id : int, k : int) -> None:
        self.id = id
        self.k = k
        self.root = treeNode.TreeNode(True, k, self.id)
    
    def __str__(self):
        q = deque([self.root])
        s = ""
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                if cur.bucket:
                    s += "B "
                else:
                    s +="O "
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            s+="\n"
        return s
    
    def insertNewNode(self, id : int) -> None:
        if id == self.id:
            print("Why am I adding myself")
            return
        currentNode = self.root
        parent = None
        movementBits = ~(id^self.id) #0 if bits were not same, else 1
        bitMask = 1
        currentInsertIdBit = id
        while bitMask&movementBits == 1:
            moveBit = bitMask&currentInsertIdBit
            #TODO seperate insertion and traversal instead of doing both at the same time its really confusing right now
            if (moveBit and not currentNode.right) or (not moveBit and not currentNode.left) : #TODO NEED TO ADD THE traversal version of this (no insertion)
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
                    parent = newSubRoot
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
                    parent = newRoot
            movementBits >>= 1
            currentInsertIdBit >>= 1
        #will leave you at the node you last agreed on!
        moveBit = bitMask&currentInsertIdBit
        if parent:
            newSubRoot = treeNode.TreeNode(False, self.k, 0)
            newLeaf = treeNode.TreeNode(True, self.k, id)
            if parent.right is currentNode:
                parent.right = newSubRoot
            else:
                parent.left = newSubRoot
            if moveBit:
                newSubRoot.right = currentNode
                newSubRoot.left = newLeaf
            else:
                newSubRoot.left = currentNode
                newSubRoot.right = newLeaf
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
        #while lsb the same
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