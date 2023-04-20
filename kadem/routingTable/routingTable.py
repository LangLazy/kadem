from dataStructures import treeNode
from collections import deque 

class RoutingTable:
    #id - 160 bit sha1 id
    #k - global paramter which represents bucket size
    def __init__(self, id : int, k : int) -> None:
        self.id = id
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
        holder.insert(id)
    
    def __str__(self):
        q = deque([self.root])
        s = ""
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                if cur.leafHuh:
                    s += "B "
                else:
                    s +="O "
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            s+="\n"
        return s
    
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
        parent = self.root
        currentNode = parent.left
        if self.id&1 == 1:
            currentNode = parent.right
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
        #Current Node at this point will be the node in which after following the appropriate direction down will have the kbucket
        #Essentially this Node represents the longest common suffix of the HashNode id and the inserted id

    def __kBucketInsert(self, newId) -> None:
        bitMask = 1
        currentNode = self.root
        while not currentNode.leafHuh:
            if bitMask&newId:
                currentNode = currentNode.right
            else:
                currentnode = currentNode.left
            newId >>= 1
        currentNode.insert(newId)

    def insertNewNode(self, id : int) -> None:
        if id == self.id:
            raise Exception("Why am I adding myself?!")
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