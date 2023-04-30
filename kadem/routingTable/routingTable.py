from dataStructures import treeNode
from routingTable.selfAddException import SelfAddException
from collections import deque 

class RoutingTable:
    #id - 160 bit sha1 id
    #k - global paramter which represents bucket size
    def __init__(self, id : int, k : int) -> None:
        self.id = id|(1<<160) #Important so that leading zeros do not disapear
        self.k = k
        self.root = treeNode.TreeNode(False, k)
        holder = treeNode.TreeNode(True, k)
        notHolder = treeNode.TreeNode(True, k)
        if id&1 == 1:
            self.root.right = holder
            self.root.left = notHolder
        else:
            self.root.right = notHolder
            self.root.left = holder
        holder.insert(self.id )
    
    def __str__(self):
        s = ""
        cur = self.root
        while not cur.leafHuh:
            if cur.right.leafHuh and cur.left.leafHuh:
                if cur.right.isPresent(self.id):
                    s += "1"
                    cur = cur.right
                elif cur.left.isPresent(self.id):
                    s += "0"
                    cur = cur.left
            else:
                if cur.right.leafHuh:
                    s += "0"
                    cur = cur.left
                else:
                    s += "1"
                    cur = cur.right
        return s[::-1]
    
    def __splitParent(self, moveBit : int, parent : treeNode.TreeNode, currentNode : treeNode.TreeNode) -> treeNode.TreeNode:
        newLeaf = treeNode.TreeNode(True, self.k)
        newRoot  = treeNode.TreeNode(False, self.k)
        if moveBit:
            newRoot.right = currentNode
            newRoot.left = newLeaf
        else:
            newRoot.left = currentNode
            newRoot.right = newLeaf
        if parent.right is currentNode:
            parent.right = newRoot
        else:
            parent.left = newRoot
        return newRoot

    def __generatePath(self, newId : int) -> None:
        parent = None
        currentNode = self.root
        movementBits = ~(newId^self.id) #0 if bits were not same, else 1
        bitMask = 1
        currentInsertIdBit = newId
        while bitMask&movementBits == 1:
            moveBit = bitMask&currentInsertIdBit
            if (moveBit and not currentNode.right) or (not moveBit and not currentNode.left):
                parent = self.__splitParent(moveBit, parent, currentNode)
            else:
                parent = currentNode
                if moveBit:
                    currentNode = currentNode.right
                else:
                    currentNode = currentNode.left
            movementBits >>= 1
            currentInsertIdBit >>= 1
        if currentNode.leafHuh:
            moveBit = bitMask&currentInsertIdBit
            parent = self.__splitParent(moveBit^1, parent, currentNode)
        #Current Node at this point will be the node in which after following the appropriate direction down will have the kbucket
        #Essentially this Node represents the longest common suffix of the HashNode id and the inserted id

    def __kBucketInsert(self, newId) -> None:
        bitMask = 1
        currentNode = self.root
        currentBit = newId
        while not currentNode.leafHuh:
            if bitMask&currentBit:
                currentNode = currentNode.right
            else:
                currentNode = currentNode.left
            currentBit >>= 1
        currentNode.insert(newId)

    def insertNewNode(self, id : int) -> None:
        if (id|(1<<160)) == self.id:
            #Need to add a 1 bit in the 161st position so that leading zeros are perserved
            raise SelfAddException("Why am I adding myself?!")
        self.__generatePath(id)
        self.__kBucketInsert(id)
        #The Bucket Splitting Algorithm Psuedo code
        #While LSB (Least Significant Bit) is the same
            #if the appropraite direction is available (1 -> right, 0 left)
                #move in that direction
            #else
                #this means you are at the lowest kbucket which has not been expanded yet
                #you need to go to the parent change it to be a new intermediary
                #split into 2 buckets
                #move into the appropriate one
            #Shift current bit being looked at (>>)
        #After exiting the loop, current node is first bit that is different between ServerId and the Id to be inserted
        #Go up to parent - the path to this node is the longest shared prefix between the ServerId and the Id to be inserted
            #if not parent (Current node is root - id's differ at first bit) 
                # Make new parent and split and it
                # Add to needed kBucket
            #else
                # Go up to parent and see if k bucket exists
                # If yes add yourself else make the node and bucket and add yourself

    def getKClosestNodes():
        pass